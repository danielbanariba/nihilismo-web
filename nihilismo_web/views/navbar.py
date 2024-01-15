import reflex as rx 
from nihilismo_web.styles.styles import MAX_WIDTH , Size, Color
from nihilismo_web.components.link_icons import link, linkv2 #link_icon,
import nihilismo_web.url as url
from nihilismo_web.components.icons import icon
#from nihilismo_web.views.navbarv2 import navbarv2

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.center(
                rx.box(
                    rx.hstack(
                        linkv2(
                            url.MUSICA, #TODO Hacer una pagina aparte para todos los links de las diferentes plataformas de streaming
                            "MUSICA",
                            "right",
                        ),
                        link(
                            url.FACEBOOK,
                            "VIDEOS",
                            "right"  
                        ),
                        linkv2(
                            url.MERCADERIA,
                            "MERCADERIA",
                            "right",
                        ),
                    ),
                    display=["none", "none", "none", "flex", "flex"], 
                ),
                rx.box(
                        rx.hstack(
                            link(
                                url.FACEBOOK,
                                "FACEBOOK",
                                "left",
                            ),
                            link(
                                url.INSTAGRAM,
                                "INSTAGRAM",
                                "left",
                            ),  
                        ),
                        display=["none", "none", "none", "flex", "flex"],
                    ),
                rx.hstack(
                    rx.box(
                        rx.hstack(
                            linkv2(
                                url.MUSICA, 
                                "MUSICA",
                                "left",
                            ),
                            link(
                                url.FACEBOOK,
                                "VIDEOS",
                                "left"  
                            ),
                            linkv2(
                                url.MERCADERIA,
                                "MERCADERIA",
                                "left",
                            ),  
                            link(
                                url.FACEBOOK,
                                "FACEBOOK",
                                "left",
                            ),
                            link(
                                url.INSTAGRAM,
                                "INSTAGRAM",
                                "left",
                            ),  
                        ),
                        display=["none", "none", "flex", "none", "none"],
                    ),
                    rx.container(
                        rx.hstack(
                            #navbarv2(),
                            rx.box(
                                icon(
                                    url.FACEBOOK,
                                    "facebook_navbar",
                                    Size.MUY_BIG.value,
                                    Color.PRIMARY.value,
                                    "0 0 512 512"
                                ),
                                padding_right=Size.VERY_SMALL.value,
                                padding_button=Size.SMALL.value,
                            ),
                            rx.box(
                                icon(
                                    url.INSTAGRAM,
                                    "instagram_navbar",
                                    Size.MUY_BIG.value,
                                    Color.PRIMARY.value,
                                    "0 0 512 512"
                                ),
                            padding_left=Size.VERY_SMALL.value,
                            padding_button=Size.SMALL.value,
                            ),
                        display=["flex", "flex", "none", "none", "none"], 
                        ),
                    ),
                ),
                flex_direction=["column", "column", "column", "row", "row"], 
                width="100%",
            ),
            width="100%"
        ),
        bg=Color.SECONDARY.value,
        padding_x=Size.BIG.value, # El padding es el espacio que hay entre el borde y el texto
        padding_y=Size.VERY_SMALL.value,
        padding_top=Size.VERY_SMALL.value,
        width="100%",
    )