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
    
    def darValor(self):
        valor = 0;
        for c in self.cartas:
            valor += c.darValor()
        
        return valor

    def darCarta(self):
        return self.cartas.pop()

    def agregarCarta(self , carta):
        self.cartas.append(carta)

if __name__ == '__main__':
    m = mazo()
    j = mazo(True) # Mazo del jugador
    j.agregarCarta(m.darCarta())
    j.agregarCarta(m.darCarta())

    for c in j.cartas:
        print(c.mostrar())
    print(j.darValor())

#Cómo desordenar las cartas desde el principio?  -  TAREA  