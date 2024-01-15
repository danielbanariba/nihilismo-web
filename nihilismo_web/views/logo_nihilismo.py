import reflex as rx 
import datetime
import nihilismo_web.styles.styles as styles
import nihilismo_web.url as URL
from nihilismo_web.styles.styles import Size, Color, TextColor

def logo_nihilismo() -> rx.Component:
    return rx.image(
        src="img/logo-nihilismo.png"
    )