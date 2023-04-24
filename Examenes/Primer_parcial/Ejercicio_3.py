from collections import deque

def find_shortest_path(maze, start_row, start_col):
    # Inicializa la cola con la posición de inicio y la lista de movimientos
    queue = deque([(start_row, start_col, 0, [])])
    # Inicializa el conjunto de visitados con la posición de inicio
    visited = {(start_row, start_col)}
    
    # Define los posibles movimientos
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Bucle del algoritmo BFS
    while queue:
        row, col, distance, moves = queue.popleft()
        
        # Comprueba si hemos llegado a la salida
        if maze[row][col] == "E":
            return moves
        
        # Prueba a moverse en cada dirección
        for movement in movements:
            new_row = row + movement[0]
            new_col = col + movement[1]
            
            # Comprueba si la nueva posición está dentro de los límites y no es una pared
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and \
               maze[new_row][new_col] != "#" and (new_row, new_col) not in visited:
                
                # Añade la nueva posición a la cola y al conjunto de visitados
                queue.append((new_row, new_col, distance + 1, moves + [movement]))
                visited.add((new_row, new_col))
    
    # Si no se encuentra un camino, devuelve una lista vacía
    return []

maze = [
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
    ['#', ' ', ' ', 'S1', '#', '#', '#', ' ', ' ', 'S2']
]

start_row = 10
start_col = 10
moves_to_exit = find_shortest_path(maze, start_row, start_col)

if not moves_to_exit:
    print("¡No se encontró un camino!")
else:
    print("Pasos para llegar a la salida:")
    current_row, current_col = start_row, start_col
    for move in moves_to_exit:
        print(f"Moverse {move} desde ({current_row}, {current_col})")
        current_row += move[0]
        current_col += move[1]
    print("¡Has llegado a la salida!") 
