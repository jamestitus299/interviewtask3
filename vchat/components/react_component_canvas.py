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


# class Hello(NoSSRComponent):
#     # Use an absolute path starting with /public
#     library = "/public/hello"

#     # Define everything else as normal.
#     tag = "Example"

# class ContentRenderer(rx.NoSSRComponent):
#     """A component that renders different types of content."""

#     # Define the library to use
#     # library = "content-renderer"

#     # # Define the props
#     # tag = "ContentRenderer"

#     # Define the properties
#     content: Any
#     wrapper_class_name: Optional[str] = "p-4"

#     def _get_custom_code(self):
#         return """
#                 import { createElement, isValidElement } from "react"

#                 export const ContentRenderer = ({ content, wrapperClassName = "p-4" }) => {
#                     const renderContent = () => {
#                         // If content is a function, call it
#                         if (typeof content === "function") {
#                             return content();
#                         }

#                         // If content is a valid React element, render it directly
#                         if (isValidElement(content)) {
#                             return content;
#                         }

#                         // If content is a string, check if it's HTML
#                         if (typeof content === "string") {
#                             if (content.trim().startsWith("<")) {
#                                 return (
#                                     <div
#                                         dangerouslySetInnerHTML={{ __html: content }}
#                                         className="content-html"
#                                     />
#                                 );
#                             }
#                             // For plain strings, render as text
#                             return <span className="content-text">{content}</span>;
#                         }

#                         // Return null for unsupported content types
#                         return null;
#                     };

#                     return <div className={wrapperClassName}>{renderContent()}</div>;
#                 }"""

# def context_renderer() -> rx.Component:
#     # HTML string example
#     html_content = "<h1>Hello World</h1><p>This is <strong>HTML</strong> content</p>"

#     # Code example
#     code_example = "<h1> James </h1>"

#     return rx.vstack(
#         rx.heading("Content Renderer Examples", size="2"),
#         rx.box(
#             ContentRenderer.create(
#                 content=html_content,
#                 wrapper_class_name="p-4 bg-gray-100 rounded"
#             )
#         ),
#         rx.box(
#             ContentRenderer.create(
#                 content=code_example,
#                 wrapper_class_name="p-4 bg-blue-100 rounded"
#             )
#         ),
#         spacing="4",
#         padding="4",
#     )


# Convenience function to create the component.
# react = React.create
reactcanvas = LiveProvider.create
preview = LivePreview.create
editable = LiveEditable.create
error = LiveError.create
reactRunner = ReactRunner.create
# hello = ContentRenderer.create


# class State(rx.State):
#     def __init__(self):
#         super().__init__()
#         self.add_style("""
#             @import "/node_modules/bootstrap/dist/css/bootstrap.min.css";
#         """)


# Component to render react code
def show_react_component(code: str):
    """
        Renders a live preview, editable view of a react/html component
    args:
        code (str) : the code to be rendered
    Returns:
        COmponent
    """
    # return reactRunner(code=code)
    # return react()
    # State.update_code(code)
    return rx.container(
        rx.dialog.close(
            rx.button("Close", size="2"),
            position="sticky",
            top="0",
            left="0",
        ),
        # rx.scroll_area(
        reactcanvas(
            # rx.script(src="https://unpkg.com/react@18/umd/react.development.js"),
            # rx.script(src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"),
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
            id="jamestitus",
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
        stack_children_full_width=True,
    )
