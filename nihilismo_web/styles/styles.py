import reflex as rx
from enum import Enum
from .fonts import Font, FontWeight
from .colors import Color, TextColor

# Ancho maximo de la pagina web
MAX_WIDTH = "1000px"

class Size(Enum): # Tamanno de las imagenes
    ZERO = "0px !important"
    VERY_SMALL = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    PEQUENIO = "1.2em"
    LARGE = "1.5em"
    GRANDELOGO = "1.7em"
    BIG = "1.9em"
    MUY_BIG = "2.5em"
    PLATAFORMAS = "3em"
    VERY_BIG = "4em"
    GIGANTE = "8em"

#Hojas de estilos
STYLESHEETS = [
    "fonts/fonts.css", # Ir al archvivo fonts.py para ver las fuentes
]

BASE_STYLES = {
    "font_family": Font.DEFAULT.value,
    "font_weight": "bold",
    "color": TextColor.PRIMARY.value,
    "background_color": Color.PRIMARY.value,
    # # No permite que se repita la imagen
    rx.Heading: {# ? rx.<propiedad> Nos permite modificar cada propiedad en nuestro componente
         "font_family": Font.DEFAULT.value,
         "color": TextColor.PRIMARY.value,
    },
    
    rx.Link: {# Desaparece el subrayado de los links
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.SECONDARY.value, # TODO CAMBIAR AL COLOR CORRESPONDIENTE
        },
    }
}

logo_canal = dict(
    font_family=Font.LOGO_CANAL.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.GRANDELOGO.value,
    _hover={"color": "#ffc435"},#TODO cambiar al color correspondiente
)