import reflex as rx

class react_component_canvas(rx.Component):
    library = "/public/canvas"
    tag = "Canvas"

# canvas = react_component_canvas.create

def show_component():
    return rx.box(
        rx.heading("james"),
        # canvas()
    )

# import reflex as rx


# class react_component_canvas(rx.Component):
#     """Spline component."""

#     # The name of the npm package.
#     library = "@splinetool/react-spline"

#     # Any additional libraries needed to use the component.
#     lib_dependencies: list[str] = [
#         "@splinetool/runtime@1.5.5"
#     ]

#     # The name of the component to use from the package.
#     tag = "Spline"

#     # Spline is a default export from the module.
#     is_default = True

#     # Any props that the component takes.
#     scene: rx.Var[str]


# # Convenience function to create the Spline component.
# spline = react_component_canvas.create


# # Use the Spline component in your app.
# def show_component():
#     return spline(
#         scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"
#     )