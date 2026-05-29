#asi se ve el algoritmo de busqueda binaria, es necesario que el arreglo este ordenado para que funcione correctamente

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

#la funcion merge sort sirve para ordenar un arreglo, es un algoritmo de ordenamiento eficiente que utiliza la técnica de divide y vencerás
#asi se ve la sintaxis de merge_sort:

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#selection sort algoritmo de ordenamiento que selecciona el elemento más pequeño de la lista y lo coloca en la posición correcta, luego repite el proceso para el resto de la lista
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#algotimo de luhn sirve para validar números de tarjetas de crédito, se basa en un proceso de suma y verificación de dígitos para determinar si un número es válido o no
def verify_card_number(card_number):
    # 1. Eliminar espacios y guiones del string
    cleaned_number = card_number.replace(" ", "").replace("-", "")
    
    # Si la tarjeta no contiene solo números tras la limpieza, es inválida
    if not cleaned_number.isdigit():
        return "INVALID!"
        
    # 2. Invertir el número para procesarlo fácilmente de derecha a izquierda
    reversed_digits = cleaned_number[::-1]
    
    total_sum = 0
    
    # 3. Recorrer los dígitos y aplicar las reglas de Luhn
    for index, char in enumerate(reversed_digits):
        digit = int(char)
        
        # Multiplicar por 2 cada segundo dígito (índices impares en el string invertido)
        if index % 2 == 1:
            digit *= 2
            # Si el resultado es mayor a 9, restamos 9
            if digit > 9:
                digit -= 9
                
        total_sum += digit
        
    # 4. Verificar si la suma total es múltiplo de 10
    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"