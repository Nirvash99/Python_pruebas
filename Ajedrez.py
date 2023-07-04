class Tablero:
    def __init__(self):
        self.tablero = [ [None]*8 for _ in range(8) ]
        self.piezas = {'torre': 't', 'caballo': 'c', 'alfil': 'a', 'rey': 'r', 'reina': 'q', 'peon': 'p'}
        self.p_blancas = []
        self.p_negras = []
        
    # Dibujar el tablero y las piezas
    def dibujar(self):
        for n, fila in enumerate(self.tablero):
            print(n+1, ' '.join(fila))

    # Agregar una pieza al tablero
    def agregar_pieza(self, tipo_pieza, color, posicion):
        x, y = posicion
        if tipo_pieza not in self.piezas:
            raise ValueError('La pieza no está en la lista.')
        if color != 'blanco' and color != 'negro':
            raise ValueError('El color no es valido.')
        if self.tablero[x][y] != None:
            raise ValueError('Ya hay una pieza en esta posición.')

        letra_pieza = self.piezas[tipo_pieza]
        if color == 'blanco':
            self.p_blancas.append((letra_pieza, posicion))
            self.tablero[x][y] = letra_pieza.upper()
        else:
            self.p_negras.append((letra_pieza, posicion))
            self.tablero[x][y] = letra_pieza

    # Verificar que el movimiento es legal
    def verificar_movimiento(self, pos_actual, pos_futura):
        x1, y1 = pos_actual
        x2, y2 = pos_futura
        if x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7:
            raise ValueError('Movimiento fuera del tablero.')
        if self.tablero[x2][y2] != None:
            raise ValueError('Ya hay una pieza aquí.')

    # Mover una pieza
    def mover_pieza(self, pos_actual, pos_futura):
        self.verificar_movimiento(pos_actual, pos_futura)
        x1, y1 = pos_actual
        x2, y2 = pos_futura

        # Mover la pieza en la lista de piezas del color apropiado
        # La búsqueda es lineal, así que es eficiente suficiente para nuestras necesidades.
        if self.tablero[x1][y1].isupper():
            for i, (letra_pieza, posicion) in enumerate(self.p_blancas):
                if posicion == pos_actual:
                    self.p_blancas[i] = (letra_pieza, pos_futura)
        else:
            for i, (letra_pieza, posicion) in enumerate(self.p_negras):
                if posicion == pos_actual:
                    self.p_negras[i] = (letra_pieza, pos_futura)

        # Mover la pieza en el tablero
        self.tablero[x2][y2] = self.tablero[x1][y1]
        self.tablero[x1][y1] = None

# Ahora escribimos la computadora que controlará el juego
class Computadora():
    def __init__(self, color='negro'):
        self.color = color
        self.tablero = None
        
    # Mueve la computadora y modifica el tablero
    def mover(self, origen, destino):
        if self.tablero[origen[0]][origen[1]].isupper():
            raise ValueError('La computadora está intentando mover una pieza de otro jugador.')
        self.tablero.mover_pieza(origen, destino)

# Finalmente, definimos la clase Juego, que iniciará el tablero e iniciará la computadora
class Juego():
    def __init__(self):
        self.tablero = Tablero()
        
        # Crear las piezas
        for y in [0, 7]:
            self.tablero.agregar_pieza('torre', 'blanco', (y, 0))
            self.tablero.agregar_pieza('torre', 'blanco', (y, 7))
            self.tablero.agregar_pieza('torre', 'negro', (y, 0))
            self.tablero.agregar_pieza('torre', 'negro', (y, 7))
        for y in [1, 6]:
            self.tablero.agregar_pieza('caballo', 'blanco', (y, 1))
            self.tablero.agregar_pieza('caballo', 'blanco', (y, 6))
            self.tablero.agregar_pieza('caballo', 'negro', (y, 1))
            self.tablero.agregar_pieza('caballo', 'negro', (y, 6))
        for y in [2, 5]:
            self.tablero.agregar_pieza('alfil', 'blanco', (y, 2))
            self.tablero.agregar_pieza('alfil', 'blanco', (y, 5))
            self.tablero.agregar_pieza('alfil', 'negro', (y, 2))
            self.tablero.agregar_pieza('alfil', 'negro', (y, 5))
        self.tablero.agregar_pieza('rey', 'blanco', (0, 4))
        self.tablero.agregar_pieza('rey', 'negro', (7, 4))
        self.tablero.agregar_pieza('reina', 'blanco', (0, 3))
        self.tablero.agregar_pieza('reina', 'negro', (7, 3))
        for y in [0, 1, 6, 7]:
            for x in range(8):
                self.tablero.agregar_pieza('peon', 'blanco' if y == 1 else 'negro', (y, x))

        # Crear computadoras
        self.computadora = Computadora(color='negro')
        self.computadora.tablero = self.tablero

    def jugar(self):
        self.tablero.dibujar()
        while True:
            # Solicitar al jugador blanco que mueva
            origen = input("Elige una pieza para mover (x,y): ")
            destino = input("Mueve la pieza a (x,y): ")
            origen = (int(origen.split(',')[0]), int(origen.split(',')[1]))
            destino = (int(destino.split(',')[0]), int(destino.split(',')[1]))

            # Mover la pieza
            try:
                self.tablero.mover_pieza(origen, destino)
            except ValueError as err:
                print(err.args[0])

            # Mover la computadora
            self.computadora.mover((2,0), (3,0))
            
            # Dibujar el tablero
            self.tablero.dibujar()

# Iniciar el juego
if __name__ == '__main__':
    juego = Juego()
    juego.jugar()