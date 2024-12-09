"""The main Chat app."""

import reflex as rx
import reflex_chakra as rc
from vchat.components import chat, navbar

from db.db_tables import create_db

def index() -> rx.Component:
    """The main app."""
    return rc.vstack(
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
create_db()

# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="teal",
    ),
)
app.add_page(index)