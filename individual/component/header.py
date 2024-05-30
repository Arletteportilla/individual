import reflex as rx 

def header()-> rx.Component:
    return rx.grid(
        rx.center(
            rx.box(
                rx.heading("Portafolio Profesional 2024", size="4"),
                rx.heading("Estudiante Uide", size="3"),
            rx.link(
                    rx.button("Abrir CV", size="2", variant="outline", margin_top="3rem", color_scheme="blue"),
                    href="https://arletteportilla.github.io/CV-main/",
                    is_external=True,
                ),    

            )
        ),
        rx.center(
            rx.image( 
                src="yo.jpg",
                alt="Imagen del portafolio",
                width="200px",
                height="auto",
                )
        ),
        columns="2",
        spacing="2",
        width="100%",
        
    )
