import reflex as rx

# class react_component_canvas(rx.Component):
#     library = "/public/canvas"
#     tag = "Canvas"

# canvas = react_component_canvas.create

# def show_component():

#     return rx.box(
#         rx.heading("james"),
#         canvas()
#     )


class LiveProvider(rx.Component):
    """React-live component."""

    # The name of the npm package.
    library = "react-live@4.1.8"

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
    library = "react-live@4.1.8"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview 
    tag = "LivePreview"

class LiveEditable(rx.Component):
    """React-live component."""

    # The name of the npm package.
    library = "react-live@4.1.8"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview 
    tag = "LiveEditor"

class LiveError(rx.Component):
    """React-live component."""

    # The name of the npm package.
    library = "react-live@4.1.8"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = []

    # The name of the component to use from the package.
    # LiveProvider, LiveEditor, LiveError, LivePreview 
    tag = "LiveError"


# Convenience function to create the Spline component.
reactcanvas = LiveProvider.create
preview = LivePreview.create
editable = LiveEditable.create
error = LiveError.create

class State(rx.State):
    code: str


# Use the component in your app.
def show_live_component():
    return rx.container(
        rx.heading("React component"),
        reactcanvas(preview(), editable(), error(), code=State.code)
    )