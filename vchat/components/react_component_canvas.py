import reflex as rx
from typing import Any, Dict, List, Optional


# This is a reflex wrapper of the react-live packgage
# class LiveProvider(rx.Component):
#     """React-live component."""

#     library = "react-live-runner"
#     # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
#     tag = "LiveProvider"
#     code: rx.Var[str]
#     scope: rx.Var[List]


# class LivePreview(rx.Component):
#     """React-live component that shows the live view of the component"""

#     library = "react-live-runner"
#     # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
#     tag = "LivePreview"


# class LiveEditable(rx.Component):
#     """React-live component that shows the editable code of the component"""

#     library = "react-live-runner"
#     # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
#     tag = "LiveEditor"


# class LiveError(rx.Component):
#     """React-live component that shows the errors"""

#     library = "react-live-runner"
#     # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
#     tag = "LiveError"


# class React(rx.Component):
#     """React-live component that shows the errors"""

#     library = "react"
#     is_default=True
#     # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
#     tag = "React"


# class UseState(rx.NoSSRComponent):
#     """React-live component that shows the errors"""

#     library = "react"
#     # lib_dependencies: list[str] = ["react", "react-dom", "@babel/standalone", "react-runner", "react-simple-code-editor", "prism-react-renderer", "sucrase"]
#     tag = "useState"


# Convenience function to create the component.
# react = React.create
# reactcanvas = LiveProvider.create
# preview = LivePreview.create
# editable = LiveEditable.create
# error = LiveError.create
# reactRunner = ReactRunner.create
# hello = ContentRenderer.create


class ReactCanvas(rx.Component):
    library = "/public/react_runner"
    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # is_default = True

    # The name of the component to use from the package.
    tag = "ReactRunner"
    code: rx.Var[str]
    preview: rx.Var[bool]
    editor: rx.Var[bool]
    error: rx.Var[bool]


# Component to render react code
def show_react_component(
    code: str, preview: bool = True, editor: bool = True, error: bool = True
):
    """
        Renders a live preview, editable view of a react component
    args:
        code (str) : the code to be rendered
    Returns:
        Component
    """

    return rx.container(
        rx.vstack(
            rx.dialog.close(
                rx.button("Close", size="2"),
                position="sticky",
                top="0",
                left="0",
            ),
            # rx.heading(
            #     "React Component",
            #     align="center",
            #     justify="center",
            #     margin_bottom="10px",
            # ),
            ReactCanvas(code=code, preview=preview, editor=False, error=error),
        ),
        background_color="white",
    )
