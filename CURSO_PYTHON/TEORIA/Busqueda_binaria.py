def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        
        if value == value_at_middle:
            return path_to_target, f"Valor encontrado en el índice {mid}"
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1
            
    return [], "Value not found"

# Llamadas de prueba para la consola
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))

#el método de búsqueda binaria, utiliza una búsqueda binaria para encontrar las raíces de una función de valor real.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#metodo de biseccion usado por la busqueda binaria, se usa diviendo el problema en problemas mas pequeños 
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # 1. Validación de negativos
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
        
    # 2. Casos especiales para 0 y 1
    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    # 3. Inicialización de límites de bisección
    low = 0.0
    high = max(1.0, square_target)
    
    for i in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid ** 2
        
        # Si cumple con el margen de error (tolerancia)
        if abs(square_mid - square_target) < tolerance:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid
        
        # Ajuste de límites según el resultado
        if square_mid > square_target:
            high = mid
        else:
            low = mid
            
    # 4. Si se agotan las iteraciones sin éxito
    print(f"Failed to converge within {max_iterations} iterations")
    return None