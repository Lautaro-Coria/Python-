# Definimos un grafo ponderado con nodos y distancias (listas de tuplas).
# Cada clave es un nodo, y cada valor es una lista de (vecino, peso/distancia).
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Implementación del algoritmo de Dijkstra para encontrar caminos más cortos
def shortest_path(graph, start, target = ''):
    # Lista de nodos no visitados (se inicializa con todos los nodos del grafo).
    unvisited = list(graph)

    # Diccionario de distancias: 0 para el nodo inicial, infinito para los demás.
    distances = {node: 0 if node == start else float('inf') for node in graph}

    # Diccionario de caminos: cada nodo comienza con una lista vacía.
    paths = {node: [] for node in graph}
    # El nodo de inicio se registra en su propio camino.
    paths[start].append(start)

    # Mientras queden nodos sin visitar...
    while unvisited:
        # Se selecciona el nodo con la distancia más corta conocida hasta ahora.
        current = min(unvisited, key=distances.get)

        # Se recorren los vecinos del nodo actual.
        for node, distance in graph[current]:
            # Si encontramos un camino más corto hacia "node" pasando por "current"...
            if distance + distances[current] < distances[node]:
                # Actualizamos la nueva distancia más corta encontrada.
                distances[node] = distance + distances[current]

                # Si la ruta previa contenía al nodo mismo, la reemplazamos.
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                # Caso contrario, extendemos el camino actual.
                else:
                    paths[node].extend(paths[current])

                # Finalmente agregamos el nodo actual al camino.
                paths[node].append(node)

        # Una vez procesado, quitamos el nodo actual de la lista de no visitados.
        unvisited.remove(current)

    # Definimos qué nodos mostrar: el "target" específico o todos si está vacío.
    targets_to_print = [target] if target else graph

    # Imprimimos la distancia y camino encontrado para cada nodo destino.
    for node in targets_to_print:
        # No mostramos la distancia del nodo hacia sí mismo.
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    # Retornamos las estructuras finales para poder usarlas más tarde.
    return distances, paths

# Llamamos a la función pidiendo el camino más corto desde 'A' hasta 'F'.
shortest_path(my_graph, 'A', 'F')