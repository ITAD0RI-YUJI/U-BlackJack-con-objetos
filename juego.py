from main import *

class juego:
    def __init__(self):
        self.mazo = mazo()
        self.casa = mazo(True)
        self.jugador = mazo(True)
    
    def iniciarJuego(self): 
        self.casa.agregarCarta(self.mazo.darCarta())
        self.casa.agregarCarta(self.mazo.darCarta())
        self.jugador.agregarCarta(self.mazo.darCarta())
        self.jugador.agregarCarta(self.mazo.darCarta())

    def mostrarJuego(self):
        print("\n• JUGADOR: ") 
        self.jugador.mostrarCartas()

        print("\n• CASA: ")
        self.casa.mostrarCartas()