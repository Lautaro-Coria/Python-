#algoritmo de búsqueda de caminos más cortos (Dijkstra)
INF = float('inf')
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)
    distances = [INF] * n
    distances[start_node] = 0
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n

    for _ in range(n):
        min_distance = INF  
        current = -1  
        for node_no in range(n):  
            if not visited[node_no] and distances[node_no] < min_distance:  
                min_distance = distances[node_no]  
                current = node_no  

        if current == -1:  
            break  
        visited[current] = True  

        for node_no in range(n):  
            distance = matrix[current][node_no]  
            if distance != INF and not visited[node_no]:  
                new_distance = distances[current] + distance  
                if new_distance < distances[node_no]:  
                    distances[node_no] = new_distance  
                    paths[node_no] = paths[current] + [node_no]

    targets = [target_node] if target_node is not None else range(n)


#--------------------------------------------------------------------------------------------------
#construir un conventidor de lista de adyacencia en una matriz de adyacencia: 
def adjacency_list_to_matrix(adjacency_list):
    # 1. Averiguamos la cantidad de nodos (longitud del diccionario)
    n = len(adjacency_list)
    
    # 2. Creamos una matriz cuadrada de n x n llena de ceros
    matrix = [[0] * n for _ in range(n)]
    
    # 3. Recorremos la lista de adyacencia para marcar las conexiones con 1
    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
            
    # 4. Imprimimos cada fila de la matriz como pide la consigna
    for row in matrix:
        print(row)
        
    # 5. Devolvemos la matriz resultante
    return matrix

#--------------------------------------------------------------------------------------------------
#implementar el algoritmo de busqueda por amplitud (BFS) para encontrar el camino más corto entre dos nodos en un grafo representado como lista de adyacencia:
def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be at least 1'
    
    queue = [('', 0, 0)]
    result = []
    while queue:
        current, opens_used, closes_used = queue.pop(0)
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))
    
    return result
print(gen_parentheses(2))


#----------------------------------------------------------------------------------------------
#construimos el algorito de busqueda en profundidad (DFS) para encontrar el camino más corto entre dos nodos en un grafo representado como lista de adyacencia:
def dfs(matrix, start_node):
    # 1. Averiguamos la cantidad total de nodos en el grafo
    n = len(matrix)
    
    # 2. Inicializamos la pila con el nodo de inicio y una lista para el orden de visitas
    stack = [start_node]
    visited = []
    
    # 3. Ciclo principal: mientras la pila no esté vacía
    while stack:
        # Sacamos el último elemento agregado (LIFO)
        current = stack.pop()
        
        # Si el nodo actual no fue visitado, lo procesamos
        if current not in visited:
            visited.append(current)
            
            # Recorremos los vecinos en orden inverso para mantener un orden consistente
            for neighbor in range(n - 1, -1, -1):
                # Si hay conexión (1) y el vecino no fue visitado, va a la pila
                if matrix[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
                    
    # 4. Devolvemos la lista de todos los nodos accesibles en el orden visitado
    return visited

#----------------------------------------------------------------------------------------------
#implementamos el algoritmo de búsqueda por profundidad (DFS) para encontrar el camino más corto entre dos nodos en un grafo representado como lista de adyacencia:
def dfs(matrix, start_node):
    stack = [start_node]
    visited = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            for neighbor in range(len(matrix[current]) - 1, -1, -1):
                if matrix[current][neighbor] == 1:
                    stack.append(neighbor)

    return visited