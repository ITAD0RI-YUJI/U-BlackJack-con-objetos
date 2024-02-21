from random import shuffle

class carta:
    def __init__(self , valor , pinta):
        self.valor = valor
        self.pinta = pinta

    def mostrar(self):
        return self.valor + " " + self.pinta

    def darValor(self): 
        if self.valor in ['J' , 'Q' , 'K']:
            return 10
        if self.valor == 'A':
            return 1 
        return int(self.valor)
    
class mazo:
    def __init__(self , jugador = False):
        if jugador:
            self.cartas = []
        else:
            self.cartas = [carta(v , p) for v in ['A' , 'J' , 'Q' , 'K'] + [str(x) for x in range(2 , 11)] 
                                        for p in ['♠' , '♥' , '♦' , '♣']]
            shuffle(self.cartas)
   
    def darValor(self):
        valor = 0;
        for c in self.cartas:
            valor += c.darValor()
        if self.tienesAs() and valor <= 11:
            valor += 10
        return valor

    def tienesAs(self):
        for c in self.cartas:
            if c.valor == 'A':
                return True
        return False

    def darCarta(self):
        return self.cartas.pop()

    def agregarCarta(self , carta):
        self.cartas.append(carta)

    def mostrarCartas(self , todas = False):
        if todas:
            print(self.cartas[0].mostrar())
        else:
            print("* *")
        
        for c in self.cartas[1:]: # Recorre desde el elemento 2, o sea el elemento 1 no lo muestra
            print(c.mostrar())

if __name__ == '__main__':
    m = mazo()
    j = mazo(True) # Mazo del jugador
    j.agregarCarta(m.darCarta())
    j.agregarCarta(m.darCarta())

    for c in j.cartas:
        print(c.mostrar())
    print(j.darValor())


# DUDA: las variables que se crean dentro del objeto, son globales en ese objeto? (o sea todo lo que esté dentro de ese objeto puede acceder a ella?) 