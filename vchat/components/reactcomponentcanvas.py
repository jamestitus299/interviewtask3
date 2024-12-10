import reflex as rx

class react_component_canvas(rx.Component):
    library = "/public/canvas"
    tag = "Canvas"

canvas = react_component_canvas.create

def show_component():
    return rx.box(
        rx.heading("james"),
        canvas
    )

# import reflex as rx


# class react_component_canvas(rx.Component):
#     """React-live component."""

#     # The name of the npm package.
#     library = "react-live"

#     # Any additional libraries needed to use the component.
#     lib_dependencies: list[str] = []

#     # The name of the component to use from the package.
#     # LiveProvider, LiveEditor, LiveError, LivePreview 
#     tag = "LiveProvider"

#     # # Spline is a default export from the module.
#     # is_default = True

#     # # Any props that the component takes.
#     code: rx.Var[str]


# # Convenience function to create the Spline component.
# reactcanvas = react_component_canvas.create

# code = "<h1>Hello james </h1>"
# # Use the Spline component in your app.
# def show_component():
#     return reactcanvas(
#         rx.heading("React component"),
#         code=code
#     )