import reflex as rx
from vchat.app_state import app_state


def sidebar_chat(chat: str) -> rx.Component:
    """A sidebar conversation items, to select and delete conversation."""
    return rx.drawer.close(
        rx.hstack(
            rx.button(
                chat,
                on_click=lambda: app_state.set_conversation(chat),
                width="80%",
                variant="surface",
            ),
            rx.button(
                rx.icon(
                    tag="trash",
                    on_click=app_state.delete_conversation,
                    stroke_width=1,
                ),
                width="20%",
                variant="surface",
                color_scheme="red",
            ),
            width="100%",
        )
    )


def sidebar(trigger) -> rx.Component:
    """The sidebar component. Contains list of conversations"""
    return rx.drawer.root(
        rx.drawer.trigger(trigger),
        rx.drawer.overlay(),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.heading("Chats", color=rx.color("mauve", 11)),
                    rx.divider(),
                    rx.foreach(app_state.conversation_titles, lambda chat: sidebar_chat(chat)),
                    align_items="stretch",
                    width="100%",
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="2em",
                background_color=rx.color("mauve", 2),
                outline="none",
            )
        ),
        direction="left",
    )


def modal(trigger) -> rx.Component:
    """A modal to create a new conversation."""
    return rx.dialog.root(
        rx.dialog.trigger(trigger),
        rx.dialog.content(
            rx.hstack(
                rx.input(
                    placeholder="Name your conversation...",
                    on_blur=app_state.set_new_conversation_name,
                    width=["15em", "20em", "30em", "30em", "30em", "30em"],
                ),
                rx.dialog.close(
                    rx.button(
                        "Create chat",
                        on_click=app_state.create_conversation,
                    ),
                ),
                spacing="2",
                width="100%",
            ),
        ),
    )


def navbar():
    """The navbar"""
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.avatar(fallback="GC", variant="solid"),
                rx.heading(
                    "Component Genie",
                    size=rx.breakpoints(
                        initial="2", xs="2", sm="4", lg="6"
                    ),
                ),
                rx.desktop_only(
                    rx.badge(
                        app_state.current_conversation,
                        rx.tooltip(
                            rx.icon("zap", size=14),
                            content="The current selected chat.",
                        ),
                        variant="soft",
                    )
                ),
                align_items="center",
            ),
            rx.hstack(
                modal(rx.button("+ New chat")),
                sidebar(
                    rx.button(
                        rx.icon(
                            tag="messages-square",
                            color=rx.color("mauve", 12),
                        ),
                        background_color=rx.color("mauve", 6),
                    )
                ),
                align_items="center",
            ),
            justify_content="space-between",
            align_items="center",
        ),
        backdrop_filter="auto",
        backdrop_blur="lg",
        padding="12px",
        border_bottom=f"1px solid {rx.color('mauve', 3)}",
        background_color=rx.color("mauve", 2),
        position="sticky",
        top="0",
        z_index="100",
        align_items="center",
    )
