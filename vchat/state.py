import os
import reflex as rx
import google.generativeai as genai
from dotenv import load_dotenv
from vchat.utils.utils_functions import make_question

load_dotenv()

# Checking if the API key is set properly
if not os.getenv("GEMINI_API_KEY"):
    raise Exception("Please set GEMINI_API_KEY environment variable. Follow the setup in the readme")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class QA(rx.Base):
    """A question and answer pair."""
    question: str
    answer: str
    code : bool
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

        # Check if the question is empty
        if question == "":
            return
        
        prompt = question
        # prompt = make_question(question)
        # print(len(question))
        # print(len(prompt))
        
        # Add the question to the list of questions.
        qa = QA(question=question, answer="", code=True, processing=False)
        self.chats[self.current_chat].append(qa)

        # # Clear the input and start the processing.
        self.processing = True
        self.chats[self.current_chat][-1].processing = True
        yield

        try: 
            # 
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            answer = response.text
            # print(question)
            # print(answer)
            # # Ensure answer is not None before concatenation
            if answer is not None:
                # self.chats[self.current_chat][-1].answer = answer
                pass
            else:
                # Handle the case where answer_text is None, perhaps log it or assign a default value
                # For example, assigning an empty string if answer_text is None
                answer = "Could not process your query. Please try again."
        except Exception as e:
            print(e)
            self.chats[self.current_chat][-1].code = False
            answer = "Could not process your query. Try again after some time."
        finally:
            self.chats[self.current_chat][-1].answer = answer
            yield
                
        # Toggle the processing flag.
        self.chats[self.current_chat][-1].processing = False
        self.processing = False