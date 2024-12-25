import reflex as rx
from typing import Any, Dict, Optional


# This is a reflex wrapper of the react-live packgage
class LiveProvider(rx.Component):
    """React-live component."""

    library = "react-live-runner"
    # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
    tag = "LiveProvider"
    code: rx.Var[str]


class LivePreview(rx.Component):
    """React-live component that shows the live view of the component"""

    library = "react-live-runner"
    # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
    tag = "LivePreview"


class LiveEditable(rx.Component):
    """React-live component that shows the editable code of the component"""

    library = "react-live-runner"
    # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
    tag = "LiveEditor"


class LiveError(rx.Component):
    """React-live component that shows the errors"""

    library = "react-live-runner"
    # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
    tag = "LiveError"


# class Hello(rx.NoSSRComponent):
#     library = "/public/hello"
#     # Any additional libraries needed to use the component.
#     lib_dependencies: list[str] = []

#     # is_default = True

#     # The name of the component to use from the package.
#     tag = "UseRunner"


# Convenience function to create the component.
# react = React.create
# reactcanvas = LiveProvider.create
# preview = LivePreview.create
# editable = LiveEditable.create
# error = LiveError.create
# reactRunner = ReactRunner.create
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
    # scope =[jsx]
    reactcanvas = LiveProvider.create
    preview = LivePreview.create
    editable = LiveEditable.create
    error = LiveError.create

    return rx.container(
        rx.dialog.close(
            rx.button("Close", size="2"),
            position="sticky",
            top="0",
            left="0",
        ),
        # rx.script(
        #     src="https://unpkg.com/react@18/umd/react.production.min.js",
        #     cross_origin="anonymous",
        # ),
        # rx.script(
        #     src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js",
        #     cross_origin="anonymous",
        # ),
        # rx.script(
        #     src="https://unpkg.com/@babel/standalone/babel.min.js",
        #     cross_origin="anonymous",
        # ),
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
                            # background_color="black",
                            type="always",
                            scrollbars="both",
                            # padding="8",
                            style={"height": "60vh", "width": "90vh"},
                            border_radius=".5em",
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
            # scope=react
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
        # id="jamestitus",
        padding="0px",
    )
