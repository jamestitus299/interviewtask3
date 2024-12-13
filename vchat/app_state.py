from typing import List, Optional
from aiolimiter import AsyncLimiter
import reflex as rx
import asyncio
from datetime import datetime
from vchat.utils.custom_exceptions import RateLimitExceeded
from vchat.utils.genai_LLM import get_ans_from_LLM
from vchat.utils.utils_functions import (
    check_prompt_is_for_react,
    check_text_for_html_code,
    check_text_for_jsx_code,
)
from vchat.utils.logger import logger

# logger for the application
logger = logger


class QA(rx.Base):
    """The chat format for transfer between backend and frontend"""

    question: str  # the question (prompt)
    text: str  # the text (description) received from LLM
    code: str  # the code received from LLM
    is_code: int  # if the response from LLM is a code
    processing: bool  # flag to indicate whether question is being processed


# Dictionary to store conversation data
# Key: Conversion name (str)
# Value: List of chat messages (list)
CHATS = {
    "Chats": [],
}


class app_state(rx.State):
    """The main application state."""

    # A dict from the chat name to the list of questions and answers.
    chats: dict[str, list[QA]] = CHATS

    # The current conversation name. A conversation is single page of chats
    current_conversation = "Chats"

    # The current question.
    question: str

    # flag to check if the question is currently being processed
    processing: bool = False

    # The name of the new conversation.
    new_conversation_name: str = ""

    # for rate limiting (30 requests in one hour)
    request_count: int = 0
    last_request_time: str = None
    max_requests: int = 30  # Maximum requests allowed
    time_window: int = 3600  # time in seconds

    def check_rate_limit(self) -> bool:
        """Check if the request should be rate limited

        Returns:
            bool: True if allowed, False if rate exceeded
        """
        current_time = datetime.now()
        # print(self.request_count)
        # print(self.last_request_time)

        # Initialize last_request_time if it's None
        if not self.last_request_time:
            self.last_request_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.request_count = 1
            return True

        # Reset count if time window has passed
        last_time = datetime.strptime(self.last_request_time, "%Y-%m-%d %H:%M:%S")
        time_diff = current_time - last_time
        time_diff = time_diff.total_seconds()
        if time_diff > self.time_window:
            self.request_count = 0
            self.last_request_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            return True

        self.request_count += 1
        # Check if the rate limit has been reached/exceeded
        if self.request_count >= self.max_requests:
            return False
        return True

    def create_conversation(self):
        """Create a new conversation."""
        # Add the new chat to the list of chats.
        self.current_conversation = self.new_conversation_name
        self.chats[self.new_conversation_name] = []

    def delete_conversation(self):
        """Delete the current chat."""
        del self.chats[self.current_conversation]
        if len(self.chats) == 0:
            self.chats = CHATS
        self.current_conversation = list(self.chats.keys())[0]

    def set_conversation(self, chat_name: str):
        """Set the name of the current chat.

        Args:
            chat_name: The name of the chat.
        """
        self.current_conversation = chat_name

    @rx.var
    def conversation_titles(self) -> list[str]:
        """Get the list of chat titles.

        Returns:
            The list of chat names.
        """
        return list(self.chats.keys())

    async def genai_process_question(self, form_data: dict[str, str]):
        """Get the response from the LLM model.

        Args:
            form_data: question (prompt)
        """

        logger.info("Request received")
        # print("----request received-----")

        question = form_data["question"]
        # Check if the question is empty
        if question == "":
            return
        prompt = question

        # Add the question to the list of questions, to the conversation
        qa = QA(question=question, text="", code="", is_code=0, processing=False)
        self.chats[self.current_conversation].append(qa)
        # Flags for rendering loading animation.
        self.processing = True
        self.chats[self.current_conversation][-1].processing = True
        yield

        # check rate limiter
        if not self.check_rate_limit():
            # Create a new QA object for the rate limit message
            qa = QA(
                question=form_data["question"],
                text="Rate limit exceeded. Please trying after some time.",
                code="",
                is_code=0,
                processing=False,
            )
            self.chats[self.current_conversation].append(qa)
            return

        try:
            # send prompt to LLM and get response
            async def get_response(prompt):
                LLM_response = get_ans_from_LLM(prompt)
                return LLM_response

            # Wait for a response with a timeout of 60 seconds
            LLM_response = await asyncio.wait_for(get_response(prompt), timeout=45)
            desc, code = LLM_response

            # Check Code generated by LLM is HTML or react code
            # (html-1) (react-2) for rendering in the frontend
            if code is not None:
                if check_text_for_html_code(code):
                    self.chats[self.current_conversation][-1].is_code = 1
                else:
                    self.chats[self.current_conversation][-1].is_code = 2
                self.chats[self.current_conversation][-1].text = desc
                self.chats[self.current_conversation][-1].code = code
                yield
            else:
                # Handle the case where LLM did not generate any code, only pass generated text to frontend
                self.chats[self.current_conversation][-1].is_code = 0
                self.chats[self.current_conversation][-1].text = desc
                yield
        # except RateLimitExceeded:
        #     logging.error("Rate limit exceeded.")
        #     self.chats[self.current_conversation][-1].is_code = 0
        #     self.chats[self.current_conversation][
        #         -1
        #     ].text = "You have exceeded your limit. Try after some time."
        #     # Toggle the processing flags.
        #     self.chats[self.current_conversation][-1].processing = False
        #     self.processing = False
        #     yield
        except asyncio.TimeoutError:
            logger.error("Processing took too long and timed out.")
            self.chats[self.current_conversation][-1].is_code = 0
            self.chats[self.current_conversation][
                -1
            ].text = "Processing timed out. Please try again later."
            # Toggle the processing flags.
            self.chats[self.current_conversation][-1].processing = False
            self.processing = False
            yield
        except Exception as e:
            self.chats[self.current_conversation][-1].is_code = False
            answer = "Could not process your query. Try again after some time."
            self.chats[self.current_conversation][-1].text = answer
            yield
            print("ERROR ", e)
            logger.error(e)
        finally:
            # Toggle the processing flags.
            self.chats[self.current_conversation][-1].processing = False
            self.processing = False
            yield
