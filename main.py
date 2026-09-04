from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Title("Minimal FastHTML App"), Main(
        H1("Welcome to FastHTML! 👋"),
        P("This is a clean, minimal webpage built entirely in Python."),
        # Changed Card to Article to match standard FastHTML / Pico CSS semantics
        Article(
            H3("Why FastHTML?"),
            Ul(
                Li("Zero configuration to get started"),
                Li("Automatic responsive layout (via Pico CSS)"),
                Li("Powered by Python and HTMX under the hood")
            )
        ),
        A("Learn More", href="https://fastht.ml", cls="button"),
        cls="container"
    )

serve()