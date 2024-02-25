from juego import *

nombre_partida = input("\n• Ingresa tu nombre de usuario: ")

user = Usuario(nombre_partida)
print("\n♥ Hola ",user.User_presentation(), " bienvenido")

juego = juego()
juego.iniciarJuego()
juego.mostrarJuego() 