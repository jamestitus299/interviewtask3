import pytest
from vchat.utils.utils_functions import (
    check_prompt_is_for_html,
    check_prompt_is_for_react,
    check_text_for_html_code,
    check_text_for_jsx_code,
)


# Test cases for check_prompt_is_for_html
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Can you create an HTML page for me?", 1),
        ("Please write some html code", 1),
        ("I need help with HTML and CSS", 1),
        ("Write a Python script", 0),
        ("", 0),
        ("HTML", 1),
        ("html", 1),
        ("HTML in this text", 1),
    ],
)
def test_check_prompt_is_for_html(input_text: str, expected: bool):
    result = check_prompt_is_for_html(input_text)
    assert result == expected


# Test cases for check_prompt_is_for_react
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Can you create a React component?", 1),
        ("Please write some react code", 1),
        ("I need help with React and JavaScript", 1),
        ("Write a Python script", 0),
        ("", 0),
        ("REACT", 1),
        ("react", 1),
        ("React in this text", 1),
    ],
)
def test_check_prompt_is_for_react(input_text: str, expected: bool):
    result = check_prompt_is_for_react(input_text)
    assert result == expected


# Test cases for check_text_for_html_code
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("<!DOCTYPE html>\n<html><body></body></html>", 1),
        ("```html\n<div>Hello</div>\n```", 1),
        ("Here's some regular text", 0),
        ("", 0),
        ("Just the word html", 0),
        ("<div>This looks like HTML but isn't marked properly</div>", 0),
    ],
)
def test_check_text_for_html_code(input_text: str, expected: bool):
    result = check_text_for_html_code(input_text)
    assert result == expected


# Test cases for check_text_for_jsx_code
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("```jsx\nfunction App() { return <div>Hello</div> }\n```", 1),
        ("Here's some regular text", 0),
        ("", 0),
        ("Just the word jsx", 0),
        ("function App() { return <div>Hello</div> }", 0),
    ],
)
def test_check_text_for_jsx_code(input_text: str, expected: bool):
    result = check_text_for_jsx_code(input_text)
    assert result == expected
