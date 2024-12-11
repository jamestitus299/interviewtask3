import reflex as rx
from reflex.components.component import NoSSRComponent
import json
from typing import Any, Dict, Optional

# This is a reflex wrapper of the react-live packgage
class LiveProvider(rx.Component):
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


class LivePreview(rx.Component):
    """React-live component."""

    # The name of the npm package.
    library = "react-live-runner"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview
    tag = "LivePreview"


class LiveEditable(rx.Component):
    """React-live component."""

    # The name of the npm package.
    library = "react-live-runner"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview
    tag = "LiveEditor"


class LiveError(rx.Component):
    """React-live component."""

    # The name of the npm package.
    library = "react-live-runner"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview
    tag = "LiveError"


class ReactRunner(rx.Component):
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
    lib_dependencies: list[str] = []

    is_default = True

    # The name of the component to use from the package.
    tag = "React"


class Hello(NoSSRComponent):
    # Use an absolute path starting with /public
    library = "/public/hello"

    # Define everything else as normal.
    tag = "Example"
    
class ContentRenderer(rx.Component):
    """A component that renders different types of content."""
    
    # Define the library to use
    # library = "content-renderer"
    
    # # Define the props
    # tag = "ContentRenderer"
    
    # Define the properties
    content: Any
    wrapper_class_name: Optional[str] = "p-4"

    def _get_custom_code(self):
        return """
                import { createElement, isValidElement } from "react"

                export const ContentRenderer = ({ content, wrapperClassName = "p-4" }) => {
                    const renderContent = () => {
                        // If content is a function, call it
                        if (typeof content === "function") {
                            return content();
                        }
                        
                        // If content is a valid React element, render it directly
                        if (isValidElement(content)) {
                            return content;
                        }
                        
                        // If content is a string, check if it's HTML
                        if (typeof content === "string") {
                            if (content.trim().startsWith("<")) {
                                return (
                                    <div
                                        dangerouslySetInnerHTML={{ __html: content }}
                                        className="content-html"
                                    />
                                );
                            }
                            // For plain strings, render as text
                            return <span className="content-text">{content}</span>;
                        }
                        
                        // Return null for unsupported content types
                        return null;
                    };
                    
                    return <div className={wrapperClassName}>{renderContent()}</div>;
                }"""
        
def context_renderer() -> rx.Component:
    # HTML string example
    html_content = "<h1>Hello World</h1><p>This is <strong>HTML</strong> content</p>"
    
    # Code example
    code_example = "<h1> James </h1>"
    
    return rx.vstack(
        rx.heading("Content Renderer Examples", size="2"),
        rx.box(
            ContentRenderer.create(
                content=html_content,
                wrapper_class_name="p-4 bg-gray-100 rounded"
            )
        ),
        rx.box(
            ContentRenderer.create(
                content=code_example,
                wrapper_class_name="p-4 bg-blue-100 rounded"
            )
        ),
        spacing="4",
        padding="4",
    )


# Convenience function to create the component.
react = React.create
reactcanvas = LiveProvider.create
preview = LivePreview.create
editable = LiveEditable.create
error = LiveError.create
reactRunner = ReactRunner.create
hello = ContentRenderer.create


# class State(rx.State):
#     code: str

#     # def update_code(self, code:str):
#     #     self.code = code


# Use the component in your app.
def show_live_component(code: str):
    """
        Renders a live preview, editable component of a react/html component
    args:
        code (str) : the code to be rendered as a string
    Returns:
        container
    """
    return context_renderer()
    # return hello(code)
    # State.update_code(code)
    # return rx.scroll_area(
    #     rx.center(
    #         reactcanvas(
    #             rx.container(
    #                 rx.heading("Component", align="center", justify="center"),
    #                 # rx.spacer(spacing="8"),
    #                 rx.tablet_and_desktop(
    #                     rx.hstack(
    #                         rx.spacer(spacing="2"),
    #                         rx.scroll_area(
    #                             editable(),
    #                             type="always",
    #                             scrollbars="both",
    #                             margin="2",
    #                             style={"height": "50vh", "width": "40vh"},
    #                         ),
    #                         rx.spacer(spacing="2"),
    #                         rx.container(
    #                             preview(),
    #                             background_color="white",
    #                             margin="2",
    #                             style={"height": "50vh", "width": "40vh"},
    #                         ),
    #                         justify="center",
    #                         align="center",
    #                         # min_width="60vh"
    #                     ),
    #                     # rx.spacer(spacing="2"),
    #                     rx.text(
    #                         error(),
    #                         color_scheme="red",
    #                         align="center",
    #                         justify="center"
    #                     ),
    #                 ),
    #                 rx.mobile_only(
    #                     rx.vstack(
    #                         rx.spacer(spacing="2"),
    #                         rx.scroll_area(
    #                             editable(),
    #                             type="always",
    #                             scrollbars="both",
    #                             margin="2",
    #                             style={"height": "35vh", "width": "25vh"},
    #                         ),
    #                         rx.spacer(spacing="2"),
    #                         rx.text(
    #                             error(),
    #                             color_scheme="red",
    #                             align="center",
    #                             justify="center",
    #                             text_wrap="wrap"
    #                         ),
    #                         rx.spacer(spacing="2"),
    #                         rx.container(
    #                             preview(),
    #                             background_color="white",
    #                             margin="2",
    #                             style={"height": "35vh", "width": "25vh"},
    #                         ),
    #                         justify="center",
    #                         align="center",
    #                         # min_width="60vh"
    #                     ),
    #                     # rx.spacer(spacing="2"),
    #                 ),
    #             ),
    #             type="always",
    #             scrollbars="both",
    #             code=code,
    #             # style={"height": 600, "width": 600},
    #             # scope=scope,
    #             # reactRunner(code=code)
    #         ),
    #     ),
    # )
