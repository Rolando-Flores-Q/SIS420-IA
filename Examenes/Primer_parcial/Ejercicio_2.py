
"""
EJERCICIO 2
Desarrollar un juego de dos jugadores un humano y la computadora, el juego se desarrollará en un tablero de 3 x 3, 
el juego consiste en tratar de lograr el mayor numero de marcaciones continuas, donde ganará el que tenga más uniones, 
es decir marcaciones seguidas, ya sea horizontales o verticales, donde cada jugador debe marcar el mismo número de veces, 
es decir el juego termina cuando solo queda un espacio para marcar, considere los siguientes ejemplos:
"""
import random
import os
import math

class Juego:
    def __init__(self):
        self.tablero = []
        for i in range(9):
            self.tablero.append(' ')
        self.humano = 'X'
        self.coputadora = 'O'
        # if random.randint(0, 1) == 1: # si es 1 X sera el humano
        #     self.humano = 'X'
        #     self.coputadora = 'O'
        # else: # si no O sera el humano
        #     self.humano = 'O'
        #     self.coputadora = 'X'

    # muestra el trablero 
    def ver_trablero(self): 
        print("")
        for i in range(3):
            print(" ", self.tablero[0+(i*3)], ' | ', self.tablero[1+(i*3)], ' | ', self.tablero[2+(i*3)], " ")
            if(i != 2): print("-----------------")

    def tablero_lleno(self, estado):
        return not ' ' in estado
    
    def contar_resultados(self, estado, jugador):
        contador = 0
        if estado[0] == estado[1] == jugador: contador = contador + 1
        if estado[1] == estado[2] == jugador: contador = contador + 1
        if estado[3] == estado[4] == jugador: contador = contador + 1
        if estado[4] == estado[5] == jugador: contador = contador + 1
        if estado[6] == estado[7] == jugador: contador = contador + 1
        if estado[7] == estado[8] == jugador: contador = contador + 1

        if estado[0] == estado[3] == jugador: contador = contador + 1
        if estado[3] == estado[6] == jugador: contador = contador + 1
        if estado[1] == estado[4] == jugador: contador = contador + 1
        if estado[4] == estado[7] == jugador: contador = contador + 1
        if estado[2] == estado[5] == jugador: contador = contador + 1
        if estado[5] == estado[8] == jugador: contador = contador + 1

        return contador
    
    # verifica si el juego ha finalizado
    def si_el_juego_acabo(self):
        # ver si no hay mas espacio
        if(self.tablero_lleno(self.tablero)):
            # limpiar consola
            os.system('cls')
            # verificamos las jugadas del humano
            cantidad_humano = self.contar_resultados(self.tablero, self.humano)
            cantidad_computador = self.contar_resultados(self.tablero, self.coputadora)
            if(cantidad_humano > cantidad_computador): # si gana el humano
                print('Gano el humano con', cantidad_humano, 'puntos')
                return True
            if(cantidad_computador > cantidad_humano): # si gana el computador
                print('Gano el computador con', cantidad_computador, 'puntos')
                return True
            else: # si es empate
                print('El juego finalizo empate con', cantidad_computador, 'puntos cada uno!')
                return True
        
        return False
    
    def iniciar(self):
        jugador_humano = jugadorHumano(self.humano)
        jugador_computadora = jugadorComputador(self.coputadora)

        # para empezar verificamos quien empieza
        if random.randint(0, 1) == 1: # empieza el humano
            posicion = jugador_humano.mover_humano(self.tablero)
            self.tablero[posicion] = self.humano
            juega_humano = False
        else: # empieza el computador
            posicion = jugador_computadora.mover_computadora(self.tablero)
            self.tablero[posicion] = self.coputadora
            juega_humano = True

        while True:
            os.system('cls') # limpiar consola
            print(" Turno de ", self.humano)
            self.ver_trablero()

            if juega_humano:
                # pone su jugada el humano
                juega_humano = False
                posicion = jugador_humano.mover_humano(self.tablero)
                self.tablero[posicion] = self.humano
                if(self.si_el_juego_acabo()): 
                    self.ver_trablero()
                    break
            else:
                # pone su jugada el computador
                juega_humano = True
                posicion = jugador_computadora.mover_computadora(self.tablero)
                self.tablero[posicion] = self.coputadora
                if(self.si_el_juego_acabo()): 
                    self.ver_trablero()
                    break


# hace su jugada el humano
class jugadorHumano:
    def __init__(self, letra):
        self.letra = letra
    
    def mover_humano(self, estado):
        while True:
            posicion = int(input("Ingresa tu movida entre [1-9]: "))
            print()
            # en caso de que no volvera a preguntar
            if(estado[posicion-1] == ' ' and posicion > 0 and posicion < 10): # si la casilla esta vacia ponemos su jugada
                break
        return posicion - 1 

# hace su jugada el computador
class jugadorComputador(Juego): #hereda de la clase Juego
    def __init__(self, letra):
        self.letra = letra
        self.humano_letra = 'X' if letra == 'O' else 'O'
    # a quien le toca jugar
    def jugadas(self, estado):
        n = len(estado)
        x = 0
        o = 0
        for i in range(9):
            if(estado[i] == 'X'):
                x = x+1
            if(estado[i] == 'O'):
                o = o+1
        if(self.humano_letra == 'X'):
            return 'X' if x == o else 'O'
        
        if(self.humano_letra == 'O'):
            return 'O' if x == o else 'X'
    # devuelve las posiciones vacias del tablero
    def acciones(self, estado):
        return [i for i, x in enumerate(estado) if x == ' ']
    
    # generamos un tablero nuevo donde ponemos un nuevo movimiento
    def generar_tablero(self, estado, accion):
        nuevo_estado = estado.copy()
        jugador_auxi = self.jugadas(estado)
        nuevo_estado[accion] = jugador_auxi
        return nuevo_estado
    
    def ver_ventajas(self, estado):
        if(self.contar_resultados(estado, 'X')):
            return True
        if(self.contar_resultados(estado, 'O')):
            return True
        return False
    
    def minimax(self, estado, jugador):
        max_jugador = self.humano_letra # el humano busca la maxima posicion
        # la computadora busca la minima posicion
        otro_jugador = 'O' if jugador == 'X' else 'X' 

    
        if self.tablero_lleno(estado): # si el tablero esta lleno
            return {'posicion': None, 'valor': 0} 
        
        # if(jugador == max_jugador): # si esta jugando el humano
        #     obj = {'posicion': None, 'valor': -math.inf} 
        # else: # si esta jugando la computadora
        #     obj = {'posicion': None, 'valor': math.inf} 
        
        if otro_jugador == max_jugador: # si esta jugando el humano
            contador_humano = self.contar_resultados(estado, max_jugador)
            valor = 1 * (contador_humano + 1) # multiplicamos 1 * el numero de casillas vacias +1 para evitar ceros
        else:
            contador_maquina = self.contar_resultados(estado, otro_jugador)
            valor = -1 * (contador_maquina + 1)

        obj = {'posicion': None, 'valor': valor} # retornamos un objeto
        
        for posibles_movida in self.acciones(estado): # recorremos todas las movidas posib;e
            # por cada movimiento posible, ponemos la jugada en un nuevo tablero para comprobar
            nuevo_estado = self.generar_tablero(estado, posibles_movida) 
            puntuacion = self.minimax(nuevo_estado, otro_jugador) # de forma recursiva le mandamos el jugador humano para ver sus posibles jugadas
            puntuacion['posicion'] = posibles_movida # ponemos cada posible movida

            if(jugador == max_jugador): # si esta jugando el humano
                if(puntuacion['valor'] > obj['valor']): # si la nueva puntuacion obtenida es mayor a la anterior puntucion 
                    obj = puntuacion # remplaza la nueva puntucion 
            else: # si esta jugando la maquina
                if(puntuacion['valor'] < obj['valor']):
                    obj = puntuacion
            
        return obj
    
    # realiza el movimiento de la maquina
    def mover_computadora(self, estado):
        posicion = self.minimax(estado, self.letra)['posicion']
        return posicion

if __name__ == '__main__':
    juego = Juego()
    juego.iniciar()
