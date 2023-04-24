"""
Desarrolle un programa para encontrar la salida más cercana en el siguiente laberinto:
E	 	 	 	#	 	#	#	 	 
 	#	#	 	 	 	 	 	 	 
 	#	 	 	#	 	 	#	 	#
#	 	 	 	#	 	 	 	 	#
 	 	 	 	#	#	 	#	 	 
 	#	#	 	 	#	 	 	 	S3
 	#	 	 	 	 	 	 	 	#
 	#	 	#	#	#	#	#	 	#
 	 	 	 	 	 	 	#	 	 
#	 	 	S1	#	#	#	 	 	S2

"""


import heapq

# obtenemos las posiciones en la que se encuentra el inicio y el final
def posiciones(matriz, item):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if(matriz[i][j] == item): return [i, j]
    return None

# calcular la distancia entre dos nodos
def calcular_distancia(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# encontrar el camino más corto desde un nodo inicial hasta un nodo final
def a_estrella(matriz, inicio, final):
    # nodos visitados
    visitados = []
    # cola de prioridad de nodos a visitar
    cola = [[0, inicio, []]] # una cola de una tupla de tres parametros
    while cola: # mientras exista datos en la cola
        # obtener el nodo con la menor distancia hasta el momento
        [distancia, nodo, camino] = heapq.heappop(cola) # heappop elimina y devuelve el elemento minimo
        # [distancia, nodo, camino] = cola.pop() # heappop quita un elemento de la cola y lo guarda en item_cola
        # si el nodo es el nodo final, se ha encontrado el camino más corto
        if nodo == final:
            camino.append(nodo)             
            return camino
        # si el nodo no ha sido visitado aún, agregarlo a la lista de visitados
        if nodo not in visitados:
            visitados.append(nodo)
            # agregar los nodos adyacentes a la cola de prioridad
            for (x, y) in [[0,1],[1,0],[0,-1],[-1,0]]:
                fila = nodo[0] + x 
                columna = nodo[1] + y
                # validamos para que no se salga fuera de las paredes de la matriz
                if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]) and matriz[fila][columna] != '#':
                    distancia_auxi = calcular_distancia(nodo, [fila, columna]) # [2, 4, 5, 8]  
                    heapq.heappush(cola, (distancia_auxi + distancia, [fila, columna], camino+[nodo])) # agrega a la cola y ordena en base # distancia_auxi + distancia 
                    # cola.append((distancia_auxi + distancia, [fila,columna], camino+[nodo]))
                    # cola = insertar_en_heap(cola, (distancia_auxi + distancia, [fila,columna], camino+[nodo]))
    # si no se encuentra el camino, devolver None
    return None

if __name__ == "__main__":
    laberinto = [
        ['E', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' '],
        [' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', 'S3'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        [' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' '],
        ['#', ' ', ' ', 'S1', '#', '#', '#', ' ', ' ', 'S2'],
    ]
    
    inicio = 'E'
    # determinamos cual es la salida mas sercana

    inicio_posicion = posiciones(laberinto, 'E')

    # obtener la posicion de cad salida
    posicion1 = posiciones(laberinto, 'S1')
    posicion2 = posiciones(laberinto, 'S2')
    posicion3 = posiciones(laberinto, 'S3')

    # obtenemos las distancia del inicio con las salida y lo guardamos en un array
    distancias = [
        { 'posicion': posicion1, 'distancia': calcular_distancia(inicio_posicion, posicion1) }, 
        { 'posicion': posicion2, 'distancia': calcular_distancia(inicio_posicion, posicion2) }, 
        { 'posicion': posicion3, 'distancia': calcular_distancia(inicio_posicion, posicion3) }, 
    ]
    # en base a la distancia minima tomamos el valor de la posicion
    final_posicion = min(distancias, key=lambda x: x['distancia'])['posicion']   

    camino = a_estrella(laberinto, inicio_posicion, final_posicion)
    print(camino)
