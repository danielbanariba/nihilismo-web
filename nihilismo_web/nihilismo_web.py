import reflex as rx
import nihilismo_web.styles.styles as styles
from nihilismo_web.views.footer import footer
from nihilismo_web.views.navbar import navbar
from nihilismo_web.views.inicio import inicio

combined_style = {**styles.BASE_STYLES}

def index() -> rx.Component:
    return rx.vstack(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        inicio(),
        footer(),
    )

            



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=combined_style,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-3YGHT3XJFS"),
        rx.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-3YGHT3XJFS');
            """
        ),
    ],
)

app.add_page(index)
app.compile()
