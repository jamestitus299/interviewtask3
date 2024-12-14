from bs4 import BeautifulSoup

def remove_html_head(html_content):
    """
    parse the html and remove head and return body
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # Find and remove the <head> section
    if soup.head:
        soup.head.decompose()

    # Return the modified HTML
    return str(soup)


def get_html_body(html_content):
    """
    parse the html and return body
    """
    soup = BeautifulSoup(html_content, "html.parser")

    body = soup.body

    # Return the modified HTML
    return str(body)