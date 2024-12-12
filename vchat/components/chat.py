import reflex as rx
import reflex_chakra as rc

from vchat.components import loading_icon
from vchat.app_state import QA, app_state
from vchat.components import react_component_canvas


message_style = dict(
    display="inline-block",
    padding=rx.breakpoints(
        initial="1em",
        sm=".2em",
        lg="1em",
    ),
    border_radius="8px",
    max_width=["30em", "25em", "30em", "40em", "50em", "50em"],
)


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
            margin_bottom="1em",
        ),
        rx.box(
            rx.container(
                rx.cond(
                    qa.processing,
                    rx.button(rx.spinner(loading=True), "Generating", disabled=True),
                ),
                rx.vstack(
                    rx.box(
                        rx.markdown(
                            qa.text,
                        ),
                        text_align="left",
                        margin_top="1em",
                        margin_bottom="1em",
                        # **message_style,
                        # border_radius="12px",
                        max_width=rx.breakpoints(
                            initial="100%",
                            xs="15%",
                            sm="50%",
                            md="80%",
                            lg="100%",
                        ),
                    ),
                    rx.box(
                        rx.cond(
                            qa.is_code,
                            rx.dialog.root(
                                rx.dialog.trigger(
                                    rx.button("View Component"),
                                    margin_bottom="1em",
                                ),
                                rx.dialog.content(
                                    rx.container(
                                        react_component_canvas.show_live_component(
                                            code=qa.code
                                        ),
                                    ),
                                    min_height=rx.breakpoints(
                                        initial="100%",
                                        sm="80%",
                                        lg="100%",
                                    ),
                                    min_width=rx.breakpoints(
                                        initial="100%",
                                        sm="60%",
                                        lg="80%",
                                    ),
                                ),
                            ),
                        )
                    ),
                ),
                background_color=rx.color("accent", 4),
                color=rx.color("accent", 12),
            ),
        ),
        align="center",
        justify="center",
    )


def chat() -> rx.Component:
    """List all the messages in a single conversation."""
    return rx.vstack(
        rx.box(
            rx.foreach(app_state.chats[app_state.current_chat], message), width="100%"
        ),
        py="8",
        flex="1",
        width="100%",
        max_width="65em",
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
                                    # content="Enter a question to get a response.",
                                )
                            ),
                            size="3",
                            placeholder="html/react component...",
                            text_wrap=True,
                            id="question",
                            width=["15em", "20em", "45em", "50em", "50em", "50em"],
                            required=True,
                        ),
                        rx.button(
                            rx.cond(
                                app_state.processing,
                                loading_icon(height="1em"),
                                rx.text("Send"),
                            ),
                            type="submit",
                            disabled=app_state.processing,
                        ),
                        align_items="center",
                    ),
                    is_disabled=app_state.processing,
                ),
                on_submit=app_state.genai_process_question,
                reset_on_submit=True,
            ),
            rx.text(
                "Component Genie is basically purposed to generate React/html Components, but can also answer other general question. It might return factually wrong responses. User discretion is advised.",
                text_align="center",
                font_size=rx.breakpoints(
                    initial=".75em", xs=".6em", sm=".6em", lg=".75em"
                ),
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
