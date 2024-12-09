import os
from typing import List
import google.generativeai as genai
import anthropic
from openai import OpenAI
import re
from dotenv import load_dotenv

from vchat.utils.utils_functions import check_response

api_key = None
client = None


def set_LLM_model():
    """
    configures and sets the LLM
    Raises:
        Exception: if the api_key is not set
    """
    load_dotenv()
    # Checking if the API key is set properly
    if not os.getenv("GEMINI_API_KEY"):
        raise Exception(
            "Please set GEMINI_API_KEY environment variable. Follow the setup in the readme")
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    global api_key, client
    # api_key=os.environ["CLAUDE_API_KEY"]
    client = OpenAI(
        api_key=api_key,
    )


def get_desc_code_from_response(text: str) -> List[str]:
    """
    Extracts the description and code snippets from the input text.

    Args:
        text (str): Input text containing descriptions and code blocks.

    Returns:
        list: A list with the description as the first value and the code snippets as the second value.
    """
    # Regex pattern to match code blocks
    code_pattern = r"```[\s\S]*?```"

    # Extract all code blocks
    code_snippets = re.findall(code_pattern, text)

    # Remove code blocks from the text to get the description
    description = re.sub(code_pattern, "", text).strip()

    # Remove ``` markers from code snippets
    # cleaned_code_snippets = [snippet[6:-3].strip() for snippet in code_snippets]
    code_without_imports = re.sub(
        r'import.*?;', '', code_snippets[0], flags=re.DOTALL)
    code_without_imports = re.sub(
        r'```', '', code_snippets[0], flags=re.DOTALL)
    code_without_imports = re.sub(
        r'jsx', '', code_snippets[0], flags=re.DOTALL)

    # Check for valid React component pattern
    # component_pattern = r'const\s+\w+\s*=\s*(\(\)\s*=>|function\s*\(.*?\)\s*{)'
    # component_match = re.search(component_pattern, code_without_imports)

    # if not component_match:
    #     raise ValueError('No valid React component found')

    # Transform the code by removing export statement and wrapping in return
    # transformed_code = code_without_imports.replace('export default MyComponent', '')
    transformed_code = re.sub(r'export default.*?;',
                              '', code_without_imports, flags=re.DOTALL)

    # print(transformed_code)
    # final_code = f"return ({transformed_code})"

    val = [text, ""]
    return val


def get_ans_from_LLM_Gemini(prompt: str) -> List[str]:
    """
        Sends the prompt to the LLM and returns responst as List from Gemini
    Args:
        prompt (str): the prompt to send to the LLM
    Returns:
        List[str]: A list of strings. The first value is the text description from the LLM.
        The second value is the code (if any)
    """
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(prompt)

    if not check_response(response.text):
        val = [response.text, None]
        return val
    desc, code = get_desc_code_from_response(response.text)
    # print(desc)
    # print("---------")
    # print(code)

    val = [desc, code]
    return val


def get_ans_from_LLM_Anthropic(prompt: str) -> List[str]:
    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key=api_key,
    )
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content


def chat_with_gpt(prompt):
    try:
        # Send a request to the ChatGPT API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a code generation of react components with inline css"},
                {"role": "user", "content": prompt},
            ],
            # max_tokens=150,  # Adjust the response length as needed
            # temperature=0.7  # Adjust creativity level
        )
        # Extract and return the assistant's reply
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"


def get_ans_from_LLM(prompt: str) -> List[str]:
    """
        Takes in the prompt and returns the description and code from the LLM
    Args:
        prompt (str): the prompt to the model

    Returns:
        List[str]: the list contains the text description and the code(if any) from the LLM
    """
    return get_ans_from_LLM_Gemini(prompt)
