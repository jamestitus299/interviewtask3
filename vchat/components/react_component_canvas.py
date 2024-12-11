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


class React(rx.Component):
    """React-live component."""

    # The name of the npm package.
    library = "react"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    is_default = True

    # The name of the component to use from the package.
    tag = "React"


class Hello(rx.Component):
    # Use an absolute path starting with /public
    library = "/public/hello"

    # Define everything else as normal.
    tag = "Example"


# Convenience function to create the Spline component.
react = React.create
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
    return hello()
    # State.update_code(code)
    return rx.scroll_area(
        rx.center(
            reactcanvas(
                rx.container(
                    rx.heading("Component", align="center", justify="center"),
                    # rx.spacer(spacing="8"),
                    rx.tablet_and_desktop(
                        rx.hstack(
                            rx.spacer(spacing="2"),
                            rx.scroll_area(
                                editable(),
                                type="always",
                                scrollbars="both",
                                margin="2",
                                style={"height": "50vh", "width": "40vh"},
                            ),
                            rx.spacer(spacing="2"),
                            rx.container(
                                preview(),
                                background_color="white",
                                margin="2",
                                style={"height": "50vh", "width": "40vh"},
                            ),
                            justify="center",
                            align="center",
                            # min_width="60vh"
                        ),
                        # rx.spacer(spacing="2"),
                        rx.text(
                            error(),
                            color_scheme="red",
                            align="center",
                            justify="center"
                        ),
                    ),
                    rx.mobile_only(
                        rx.vstack(
                            rx.spacer(spacing="2"),
                            rx.scroll_area(
                                editable(),
                                type="always",
                                scrollbars="both",
                                margin="2",
                                style={"height": "35vh", "width": "25vh"},
                            ),
                            rx.spacer(spacing="2"),
                            rx.text(
                                error(),
                                color_scheme="red",
                                align="center",
                                justify="center",
                                text_wrap="wrap"
                            ),
                            rx.spacer(spacing="2"),
                            rx.container(
                                preview(),
                                background_color="white",
                                margin="2",
                                style={"height": "35vh", "width": "25vh"},
                            ),
                            justify="center",
                            align="center",
                            # min_width="60vh"
                        ),
                        # rx.spacer(spacing="2"),
                    ),
                ),
                type="always",
                scrollbars="both",
                code=code,
                # style={"height": 600, "width": 600},
                # scope=scope,
                # reactRunner(code=code)
            ),
        ),
    )
