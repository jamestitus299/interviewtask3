from typing import List


def check_prompt_is_for_html(text: str):
    if "html" in text:
        return 1
    return 0


def check_prompt_is_for_react(text: str):
    if "react" in text or "code" in text or "component" in text:
        return 1
    return 0


def check_text_for_html_code(text: str):
    if "<!DOCTYPE html>" in text or "```html" in text:
        return 1
    return 0


def check_text_for_jsx_code(text: str) -> int:
    if "```jsx" in text:
        return 1
    return 0


def check_question(
    question: str, words: List[str] = ["code", "react", "component"]
) -> bool:
    """
        Checks if the question contains the word in words
    Args:
        question (str): the string question
        words (List[str]): words to check for
    Returns:
        bool
    """

    for word in words:
        if word in question:
            return True
        return False


def make_question(question: str) -> str:
    """
        Constructs the question based on the prompt (checks if the prompt is to generate a react component or a general question.)
    Args:
        question (str): the string question
    Returns:
        str : the final prompt
    """
    words = ["code", "react", "component"]
    question = question.lower()

    if check_question(question, words):
        additional_prompt = ". Give the response as an array, the description should be the first value of the array, followed by the complete code and any styling if available. if the prompt is not enough, just respond, I will need additional details to answer that."
        question += additional_prompt
        return question
    else:
        return question
