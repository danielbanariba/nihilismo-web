import reflex as rx
from nihilismo_web.styles.styles import Size, Color
import nihilismo_web.styles.styles as styles
from nihilismo_web.views.velas import velas

def inicio() -> rx.Component:
    return rx.vstack(#TODO estoy en duda si poner el inicio, es que no se xd
        rx.hstack(
            rx.center(
                rx.image(
                    src="img_nihilismo/logo-nihilismo.png",
                    id="logo-image",
                    padding_top="8vh",
                    align="center",
                ),
            ),   
        ),    
        rx.hstack(
            rx.html(#La imagen no se pueda ni hacer zoom ni moverse
                '''
                    <style>
                        body {
                            overflow-x: hidden;
                        }
                        #image-container {
                            position: relative;
                            width: 100vw;
                            height: 100vh;
                        }
                        #background-image {
                            position: absolute;
                            top: 0;
                            left: 0;
                            width: 100%;
                            height: 100%;
                            object-fit: cover;
                            z-index: -1;
                        }
                        #logo-image {
                            position: absolute;
                            top: 15%;
                            width: 20%;
                            transform: translate(-50%, -50%);
                            z-index: 1;
                        }
                    </style>
                    <div id="image-container">
                        <img id="background-image" src="img/nihilismo_portada.png" alt="Background Image">
                    </div>
                ''')
        ),
    )