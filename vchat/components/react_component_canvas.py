import reflex as rx
from reflex.components.component import NoSSRComponent
import json
from typing import Any, Dict, Optional


# This is a reflex wrapper of the react-live packgage
class LiveProvider(rx.NoSSRComponent):
    """React-live component."""

    # The name of the npm package.
    library = "react-live-runner"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview
    tag = "LiveProvider"

    # is_default = True

    # # Any props that the component takes.
    code: rx.Var[str]


class LivePreview(rx.NoSSRComponent):
    """React-live component."""

    # The name of the npm package.
    library = "react-live-runner"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview
    tag = "LivePreview"


class LiveEditable(rx.NoSSRComponent):
    """React-live component."""

    # The name of the npm package.
    library = "react-live-runner"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview
    tag = "LiveEditor"


class LiveError(rx.NoSSRComponent):
    """React-live component."""

    # The name of the npm package.
    library = "react-live-runner"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview
    tag = "LiveError"


class ReactRunner(rx.NoSSRComponent):
    """React-live component."""

    # The name of the npm package.
    library = "react-runner"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    tag = "Runner"


class React(rx.Component):
    """React-live component."""

    # The name of the npm package.
    library = "react"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = ["react-dom"]

    is_default = True

    # The name of the component to use from the package.
    tag = "React"


# Convenience function to create the component.
# react = React.create
reactcanvas = LiveProvider.create
preview = LivePreview.create
editable = LiveEditable.create
error = LiveError.create
reactRunner = ReactRunner.create
# hello = ContentRenderer.create


# Component to render react code
def show_react_component(code: str):
    """
        Renders a live preview, editable view of a react component
    args:
        code (str) : the code to be rendered
    Returns:
        Component
    """
    return rx.container(
        # rx.script(
        #     src="https://cdnjs.cloudflare.com/ajax/libs/react/16.6.3/umd/react.production.min.js"
        # ),
        # rx.script(
        #     src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/16.6.3/umd/react-dom.production.min.js"
        # ),
        # rx.script("https://unpkg.com/@babel/standalone/babel.min.js"),
        rx.dialog.close(
            rx.button("Close", size="2"),
            position="sticky",
            top="0",
            left="0",
        ),
        # rx.scroll_area(
        reactcanvas(
            rx.container(
                rx.heading(
                    "React Component",
                    align="center",
                    justify="center",
                    margin_bottom="10px",
                ),
                # rx.spacer(spacing="8"),
                rx.desktop_only(
                    rx.hstack(
                        rx.scroll_area(
                            editable(),
                            # background_color="grey",
                            type="always",
                            scrollbars="both",
                            # padding="8",
                            style={"height": "60vh", "width": "90vh"},
                            border_radius="1em",
                        ),
                        rx.spacer(spacing="6"),
                        rx.scroll_area(
                            preview(),
                            type="always",
                            scrollbars="both",
                            background_color="white",
                            # padding="6",
                            style={"height": "60vh", "width": "90vh"},
                            border_radius="1em",
                        ),
                        # justify="center",
                        # align="center",
                        # max_height="60vh",
                        # min_width="100vh",
                    ),
                    rx.button(
                        "Copy code",
                        on_click=rx.set_clipboard(code),
                        size="1",
                        align="center",
                        justify="center",
                        text_align="center",
                        margin_top="10px",
                    ),
                    rx.text(
                        error(),
                        color_scheme="red",
                        align="center",
                        justify="center",
                    ),
                ),
                rx.mobile_and_tablet(
                    rx.vstack(
                        rx.spacer(spacing="1"),
                        rx.scroll_area(
                            preview(),
                            background_color="white",
                            margin="2",
                            style={"height": "35vh", "width": "25vh"},
                        ),
                        rx.button(
                            "Copy code",
                            on_click=rx.set_clipboard(code),
                            size="1",
                            align="center",
                            justify="center",
                            text_align="center",
                        ),
                        rx.spacer(spacing="2"),
                        rx.text(
                            error(),
                            color_scheme="red",
                            align="center",
                            justify="center",
                            text_wrap="wrap",
                        ),
                        rx.spacer(spacing="2"),
                        rx.scroll_area(
                            editable(),
                            type="always",
                            scrollbars="both",
                            margin="2",
                            style={"height": "35vh", "width": "25vh"},
                            border_radius=".5em",
                        ),
                        justify="center",
                        align="center",
                        # min_width="60vh"
                    ),
                    # rx.spacer(spacing="2"),
                ),
            ),
            code=code,
            # id="jamestitus",
            # scope=react()
            # reactRunner(code=code)
        ),
        #     type="always",
        #     scrollbars="both",
        #     style={"height": "100%", "width": "100%"},
        #     # width="100%",
        # ),
        # width="100%",
        # style={"height": "auto", "width": "auto"},
        # stack_children_full_width=True,
        padding="0px",
    )
