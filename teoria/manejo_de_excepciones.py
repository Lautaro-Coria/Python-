#ejemplo 
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

#en este ejemplo dividir entre cero genera una excepción ZeroDivisionError, que es capturada por el bloque except, evitando que el programa se detenga abruptamente y mostrando un mensaje de error amigable.


#otro ejemplo utilizando los bloques else y finally: 
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')
    
#tamien se puede capturar múltiples excepciones:
try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")
    
#También puedes usar el objeto de excepción, que normalmente se asigna a otro nombre con la palabra clave as. Aquí estamos usando e como alias para el objeto de error:
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')