"""The main Chat app."""

import reflex as rx
from vchat.components import chat, navbar
from vchat.components.react_component_canvas import show_react_component
from vchat.utils.genai_LLM import set_LLM_model
# from vchat.db.db_tables import create_db

def index() -> rx.Component:
    """The main app."""
    return rx.vstack(
        rx.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"),
        navbar(),
        chat.chat(),
        chat.action_bar(),
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        min_height="100vh",
        align_items="stretch",
        spacing="0",
    )


# Create database
# create_db()

# inialize the  LLM model
set_LLM_model()

# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        appearance="dark", 
        has_background=True,
        radius="large", 
        accent_color="sky",
    ),
    stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
        "https://cdn.tailwindcss.com",
    ],
)
app.add_page(index)

