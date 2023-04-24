import time
import sys
from Nodos import Nodo
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from Metodos import Metodos


def busqueda_BPPR(nodo_inicial, solucion, visitado):
    visitado.append(nodo_inicial.get_estado()) 
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        #Bucle para recorrer 
        for i in range(0, len(solucion)-1):
            indice = i
            hijo_datos = nodo_inicial.get_estado().copy()
            temp = hijo_datos[indice]
            hijo_datos[indice] = hijo_datos[indice+1]
            hijo_datos[indice+1] = temp
            hijo = Nodo(hijo_datos)
            nodo_inicial.set_hijo(hijo)
        
        for nodo_hijo in nodo_inicial.get_hijo():
            if not nodo_hijo.get_estado() in visitado: # si el nodo hijo esta en vicitados
                # Llamada Recursiva
                Solution = busqueda_BPPR(nodo_hijo, solucion, visitado)
                if Solution is not None:
                    return Solution
        return None


if __name__ == "__main__":
    size = input("Ingrese la contraseña: ")
    solucion = []
    for i in size:
        solucion.append(int(i))
    #estado_inicial = [1, 4, 0, 0, 2, 3]
    print("Solucion", solucion)
    nodo_solucion = None
    visitado = []
    if(len(solucion) > 6): 
        sys.exit('El numero maximo de digitos que soporta el programa es 6')
    # generamos randon
    estado_inicial = Metodos.generRandon(solucion, len(solucion))
    print("Estado inicial", estado_inicial)
    # verificamos si los arreglo tiene los mismos valores en orden diferente
    todo_correcto = Metodos.logitudIguales(estado_inicial, solucion)
    if(todo_correcto == False): 
        sys.exit('Los valores entre ambos arreglos no coinciden!')

    nodo_inicial = Nodo(estado_inicial)
    inicio = time.time()
    nodo_actual = busqueda_BPPR(nodo_inicial, solucion, visitado)
    fin = time.time()

    # Mostrar Resultado
    resultado = []
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Nodos abiertos: ", len(resultado))
    print("Tiempo de ejecucion: ", fin - inicio)