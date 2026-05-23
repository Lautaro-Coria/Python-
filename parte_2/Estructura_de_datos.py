def merge_sort(array):
    # Caso base: si el array tiene 1 o 0 elementos, ya está ordenado.
    if len(array) <= 1:
        return

    # Se calcula el punto medio y se divide el array en dos mitades
    middle_point = len(array) // 2
    left_part = array[:middle_point]   # elementos desde el inicio hasta el medio
    right_part = array[middle_point:]  # elementos desde el medio hasta el final

    # Llamadas recursivas: se ordena cada mitad por separado
    merge_sort(left_part)
    merge_sort(right_part)

    # Índices para recorrer cada mitad y el array principal
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Bucle principal: compara elementos de left_part y right_part,
    # y coloca el menor en la posición actual de array.
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1  # avanzamos en la mitad izquierda
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1  # avanzamos en la mitad derecha
        sorted_index += 1  # avanzamos en el array principal

    # Si quedan elementos en left_part, se copian al array
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Si quedan elementos en right_part, se copian al array
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

if __name__ == '__main__':
    # Lista inicial (no ordenada)
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)

    # Se aplica el algoritmo de merge_sort
    merge_sort(numbers)

    # Al terminar, la lista numbers queda ordenada en su lugar
    print('Sorted array: ' + str(numbers))