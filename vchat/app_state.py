from typing import List
import reflex as rx
from vchat.utils.utils_functions import make_question
from vchat.utils.genai_LLM import set_LLM_model, get_ans_from_LLM
# import loggin

# import google.generativeai as genai
# from dotenv import load_dotenv
# import os
# load_dotenv()
# # Checking if the API key is set properly
# if not os.getenv("GEMINI_API_KEY"):
#     raise Exception("Please set GEMINI_API_KEY environment variable. Follow the setup in the readme")
# genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class QA(rx.Base):
    """The chat format for transfer between backend and frontend"""
    question: str
    text : str
    code : str
    is_code : bool
    processing : bool


CHATS = {
    "Chats": [],
}

class State(rx.State):
    """The app state."""

    # A dict from the chat name to the list of questions and answers.
    chats: dict[str, list[QA]] = CHATS

    # The current chat name.
    current_chat = "Chats"

    # The current question.
    question: str

    # Whether we are processing the question.
    processing: bool = False

    # The name of the new chat.
    new_chat_name: str = ""
    
    api_key: str

    def create_chat(self):
        """Create a new chat."""
        # Add the new chat to the list of chats.
        self.current_chat = self.new_chat_name
        self.chats[self.new_chat_name] = []

    def delete_chat(self):
        """Delete the current chat."""
        del self.chats[self.current_chat]
        if len(self.chats) == 0:
            self.chats = CHATS
        self.current_chat = list(self.chats.keys())[0]

    def set_chat(self, chat_name: str):
        """Set the name of the current chat.

        Args:
            chat_name: The name of the chat.
        """
        self.current_chat = chat_name

    @rx.var
    def chat_titles(self) -> list[str]:
        """Get the list of chat titles.

        Returns:
            The list of chat names.
        """
        return list(self.chats.keys())
    
    async def genai_process_question(self, form_data: dict[str, str]):
        """Get the response from the API.

        Args:
            form_data: A dict with the current question.
        """

        question = form_data["question"]
        # print(question)

        # Check if the question is empty
        if question == "":
            return
        
        prompt = question
        # prompt = make_question(question)
        # print(len(question))
        # print(len(prompt))
        
        # Add the question to the list of questions.
        qa = QA(question=question, text="", code ="", is_code=False, processing=False)
        self.chats[self.current_chat].append(qa)

        # Start the processing. Flags for rendering and animation.
        self.processing = True
        self.chats[self.current_chat][-1].processing = True
        yield

        try: 
            # 
            LLM_response= get_ans_from_LLM(prompt)
            print("------------------")
            print(LLM_response)
            print("------------------")
            desc, code = LLM_response
            # print(desc)
            # print(code)
            # # Ensure answer is not None before concatenation
            if desc is not None and code is not None:
                self.chats[self.current_chat][-1].is_code = True
                self.chats[self.current_chat][-1].text = desc
                self.chats[self.current_chat][-1].code = code
                yield
            else:
                # Handle the case where answer_text is None, perhaps log it or assign a default value
                # For example, assigning an empty string if answer_text is None
                # answer = "Could not process your query. Please try again."
                self.chats[self.current_chat][-1].is_code = False
                self.chats[self.current_chat][-1].text = desc
                yield
        except Exception as e:
            print("ERROR " , e)
            self.chats[self.current_chat][-1].is_code = False
            answer = "Could not process your query. Try again after some time."
            self.chats[self.current_chat][-1].text = answer
        finally:
            pass
        
        # Toggle the processing flags.
        self.chats[self.current_chat][-1].processing = False
        self.processing = False