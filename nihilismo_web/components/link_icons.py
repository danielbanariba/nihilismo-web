import reflex as rx
from nihilismo_web.styles.styles import Size

def link(url: str, alt: str, margin_side: str) -> rx.Component:
    style = {
        "margin_{}".format(margin_side): Size.SMALL.value
    }
    return rx.link(
        rx.text(
            alt,
            font_size=Size.BIG.value,
            style=style
        ),
        href=url,
        is_external=True
    )
    
def linkv2(url: str, alt: str, margin_side: str) -> rx.Component:
    style = {
        "margin_{}".format(margin_side): Size.SMALL.value
    }
    return rx.link(
        rx.text(
            alt,
            font_size=Size.BIG.value,
            style=style
        ),
        href=url
    )