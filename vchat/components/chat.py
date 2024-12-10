import reflex as rx
import reflex_chakra as rc

from vchat.components import loading_icon
from vchat.state import QA, State
from vchat.components import react_component_canvas


message_style = dict(display="inline-block", padding="1em", border_radius="8px",
                     max_width=["30em", "30em", "50em", "50em", "50em", "50em"])


def message(qa: QA) -> rx.Component:
    """A single question/answer message.

    Args:
        qa: The question/answer pair.

    Returns:
        A component displaying the question/answer pair.
    """
    return rx.box(
        rx.box(

            rx.markdown(
                qa.question,
                background_color=rx.color("mauve", 4),
                color=rx.color("mauve", 12),
                **message_style,
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.box(
            rx.container(
                rx.hstack(
                    rx.box(
                        rx.cond(
                            qa.processing,
                            rx.button(
                                rx.spinner(loading=True), "Generating", disabled=True
                            ),
                        ),
                        rx.markdown(
                            qa.answer,
                            **message_style,
                        )
                    ),
                    rx.box(
                        rx.cond(
                            qa.code,
                            rx.popover.root(
                                rx.popover.trigger(
                                    rx.button("View Component"),
                                ),
                                rx.popover.content(
                                    rx.flex(
                                        react_component_canvas.show_live_component(
                                            code="<h1>Edit me!</h1>"),
                                        rx.popover.close(
                                            rx.button("Close"),
                                        ),
                                        direction="column",
                                        spacing="9",
                                    ),
                                ),
                            ),
                        )
                    ),
                ),
                background_color=rx.color("accent", 4),
                color=rx.color("accent", 12),
            ),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
    )


def chat() -> rx.Component:
    """List all the messages in a single conversation."""
    return rx.vstack(
        rx.box(rx.foreach(
            State.chats[State.current_chat], message), width="100%"),
        py="8",
        flex="1",
        width="100%",
        max_width="50em",
        padding_x="4px",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
    )


def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.center(
        rx.vstack(
            rc.form(
                rc.form_control(
                    rx.hstack(
                        rx.input(
                            rx.input.slot(
                                rx.tooltip(
                                    rx.icon("zap", size=18),
                                    content="Enter a question to get a response.",
                                )
                            ),
                            placeholder="Type something like... Give me the react code/component that does...",
                            id="question",
                            width=["15em", "20em", "45em",
                                   "50em", "50em", "50em"],
                            required=True
                        ),
                        rx.button(
                            rx.cond(
                                State.processing,
                                loading_icon(height="1em"),
                                rx.text("Send"),
                            ),
                            type="submit",
                        ),
                        align_items="center",
                    ),
                    is_disabled=State.processing,
                ),
                on_submit=State.genai_process_question,
                reset_on_submit=True,
            ),
            rx.text(
                "Gen Component is basically purposed to generate React Components, but can also answer other general question. It might return factually wrong responses. User discretion is advised.",
                text_align="center",
                font_size=".75em",
                color=rx.color("mauve", 10),
            ),
            align_items="center",
        ),
        position="sticky",
        bottom="0",
        left="0",
        padding_y="16px",
        backdrop_filter="auto",
        backdrop_blur="lg",
        border_top=f"1px solid {rx.color('mauve', 3)}",
        background_color=rx.color("mauve", 2),
        align_items="stretch",
        width="100%",
    )
