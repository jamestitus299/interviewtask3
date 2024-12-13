from bs4 import BeautifulSoup
import re


def remove_html_head(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find and remove the <head> section
    if soup.head:
        soup.head.decompose()

    # Return the modified HTML
    return str(soup)


def get_html_body(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    body = soup.body

    # Return the modified HTML
    return str(body)


def convert_css_to_react(css_string):
    # Remove comments and normalize whitespace
    css_string = re.sub(r"/\*.*?\*/", "", css_string, flags=re.DOTALL)
    css_string = re.sub(r"\s+", " ", css_string.strip())

    # Extract style blocks
    style_blocks = re.findall(r"([^\{]+)\{([^\}]+)\}", css_string)

    # Convert to React style object
    react_styles = {}

    for selector, declarations in style_blocks:
        selector = selector.strip()

        # Convert selector to camelCase key
        if selector.startswith("."):
            key = selector[1:]  # Remove the dot for class selectors
        elif selector == "body":
            key = "body"
        else:
            key = selector

        # Parse declarations
        style_dict = {}
        declarations = declarations.strip().split(";")

        for declaration in declarations:
            if ":" in declaration:
                prop, value = declaration.split(":", 1)
                prop = prop.strip()
                value = value.strip()

                # Convert property names to camelCase
                if "-" in prop:
                    parts = prop.split("-")
                    prop = parts[0] + "".join(p.capitalize() for p in parts[1:])

                # Handle special cases
                if value != "":
                    # Remove quotes if present
                    value = value.strip("\"'")

                    # Convert numeric values
                    if re.match(r"^-?\d+\.?\d*(px|rem|em|vh|vw|%)$", value):
                        if value.endswith(("px", "rem", "em", "vh", "vw", "%")):
                            # Keep units as strings
                            value = f"'{value}'"
                    else:
                        # Add quotes to color values and other string values
                        if not value.startswith(("#", "rgb", "rgba")):
                            if value not in ("none", "inherit", "initial"):
                                value = f"'{value}'"

                    style_dict[prop] = value

        react_styles[key] = style_dict

    # Generate React styles string
    output = "const styles = {\n"

    for selector, styles in react_styles.items():
        output += f"  {selector}: {{\n"
        for prop, value in styles.items():
            output += f"    {prop}: {value},\n"
        output += "  },\n"

    output += "};\n\nexport default styles;"

    return output
