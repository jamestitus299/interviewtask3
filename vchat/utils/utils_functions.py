from typing import List

def check_response(text : str) -> bool:
    return True

def check_question(question: str, words: List[str]= ["code", "react", "component"]) -> bool:
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
