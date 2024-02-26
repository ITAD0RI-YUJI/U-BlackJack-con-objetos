from main import *

class Usuario:
    def __init__(self , nombre):
        self.nombre = nombre
    
    def User_presentation(self):
        return self.nombre

class juego:
    def __init__(self , plantarse = False):
        self.mazo = mazo()
        self.casa = mazo(True)
        self.jugador = mazo(True)
        self.plantarse = plantarse
    
    def iniciarJuego(self): 
        self.casa.agregarCarta(self.mazo.darCarta())
        self.casa.agregarCarta(self.mazo.darCarta())
        self.jugador.agregarCarta(self.mazo.darCarta())
        self.jugador.agregarCarta(self.mazo.darCarta())

    def mostrarJuego(self):
        print("\n• JUGADOR: ")  #Aprender cómo poner el nombre acá (tal vez en con herencia)
        self.jugador.mostrarCartas()

        print("\n• CASA: ")
        self.casa.mostrarCartas()

    def plantarse_function(self):
        if self.plantarse == True:
            print("\n• Te plantaste, tus puntos son:")
            mazo.mostrarCartas(True)
            mazo.darValor()
        else:
            pass