"""
Welcome to Reflex! This file outlines the steps to create a basic app.
"""
import reflex as rx
from individual.component.navbar import navbar
from individual.component.header import header
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
       # rx.color_mode.button(position="top-right"),
        rx.vstack(
           navbar(),
           header(),
       ),
        rx.logo(),
    )

app = rx.App()
app.add_page(index)
