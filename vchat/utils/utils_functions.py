def check_prompt_is_for_html(text: str) -> bool:
    """
        Check if the prompt/text contains html (prompt is requesting html code)
    Args:
        text (str): The prompt/text to check
    Returns:
        bool: True if the prompt/text contains html, False otherwise
    """
    if text is None:
        return 0
    text = text.lower()
    if "html" in text:
        return 1
    return 0


def check_prompt_is_for_react(text: str) -> bool:
    """
        Check if the prompt/text contains react (prompt is requesting react code)
    Args:
        text (str): The prompt/text to check
    Returns:
        bool: True if the prompt/text contains react, False otherwise
    """
    if text is None:
        return 0
    text = text.lower()
    if "react" in text:
        return 1
    return 0


def check_text_for_html_code(text: str) -> bool:
    """
        Check if the text contains html code
    Args:
        text (str): The text to check
    Returns:
        bool: True if the text contains html, False otherwise
    """
    if text is None:
        return 0
    if "<!DOCTYPE html>" in text or "```html" in text:
        return 1
    return 0


def check_text_for_jsx_code(text: str) -> bool:
    """
        Check if the text contains react code
    Args:
        text (str): The text to check
    Returns:
        bool: True if the text contains react, False otherwise
    """
    if text is None:
        return 0
    if "```jsx" in text:
        return 1
    return 0
