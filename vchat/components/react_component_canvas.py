import reflex as rx

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


class Hello(rx.Component):
    # Use an absolute path starting with /public
    library = "/public/hello"

    # Define everything else as normal.
    tag = "Hello"


# Convenience function to create the Spline component.
reactcanvas = LiveProvider.create
preview = LivePreview.create
editable = LiveEditable.create
error = LiveError.create
reactRunner = ReactRunner.create
hello = Hello.create


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
    # State.update_code(code)
    return rx.scroll_area(
        rx.center(
            reactcanvas(
                rx.container(
                    rx.heading("Component"),
                    # rx.text_area(code),
                    rx.container(
                        preview(),
                        background_color="white",
                        margin="20px",
                        size="4"
                    ),
                    rx.scroll_area(
                        editable(),
                        type="always",
                        scrollbars="both",
                        style={"height": 480, "width": 380},
                    ),
                    error(),
                    spacing="2"
                ),
                type="always",
                scrollbars="vertical",
                style={"height": "auto", "width": "auto"},
                code=code,
                scope=None
                # reactRunner(code=code)
            ),
        ),
    )
