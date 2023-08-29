# Definición de la función para la división
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None
    except TypeError:
        print("Error: Asegúrate de que los valores sean numéricos.")
        return None
    else:
        return result

# Solicitar números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Llamar a la función y manejar el resultado
result = divide(num1, num2)

if result is not None:
    print("El resultado de la división es:", result)
else:
    print("Hubo un error en la división.")
