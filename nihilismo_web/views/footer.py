import reflex as rx 
import datetime
import nihilismo_web.styles.styles as styles
import nihilismo_web.url as URL
from nihilismo_web.styles.styles import Size, Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.box(
                rx.span(
                    """DANIEL\nBANARIBA""",
                    style=styles.logo_canal,
                ),
            ),
            href=URL.DANIEL_BANARIBA,
            is_external=True,
            alt="Logotipo de DanielBanariba.",
        ),
        rx.span(
            rx.span(
                f" © 2023-{datetime.datetime.today().year}, ",
                font_size=Size.PEQUENIO.value,
            ),
            "TODOS LOS DERECHOS RESERVADOS.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_botoom=Size.BIG.value, # Para que se separare el texto de la parte de abajo
        padding_x=Size.BIG.value, # Responsive, se separe el texto de los lados
        spacing=Size.DEFAULT.value
    )