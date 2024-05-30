
import reflex as rx

class StateContador(rx.State):
    index: int = 0

    #Creamos metodos que nos de la clase 
    def aumentar(self):
        self.index = self.index + 1

    def disminuir(self):
        self.index = self.index - 1
    
    @rx.var
    def getIndex(self):
        return self.index

#Crear la pgina que visuzliza los componentes de reflex
@rx.page(route = "/contador",title="Contador")
def contador() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading("Contador de numeros ", size= "5"),
                rx.text("Mi primer componente de texto sobre el vstack"),
                rx.hstack(
                    rx.button("Boton de incremento ",on_click=StateContador.aumentar),
                    rx.text(StateContador.getIndex),
                    rx.button("Bton de decremento", on_click=StateContador.disminuir),
                ),
            )
        )
    )