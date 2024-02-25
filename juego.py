from main import *

class Usuario:
    def __init__(self , nombre):
        self.nombre = nombre
    
    def User_presentation(self):
        return print("\n♥ Hola ", self.nombre, " bienvenido")

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
        print("\n• JUGADOR: ")  #Aprender como poner el nombre acá (tal vez en con herencia)
        self.jugador.mostrarCartas()

        print("\n• CASA: ")
        self.casa.mostrarCartas()