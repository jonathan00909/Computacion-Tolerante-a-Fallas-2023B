import os
import time
import threading

# Obtener la ubicación del archivo .py actual
ubicacion_script = os.path.dirname(__file__)

# Función para guardar el texto en un archivo temporal
def guardar_texto(texto):
    archivo_temporal = os.path.join(ubicacion_script, 'archivo_temporal.txt')
    with open(archivo_temporal, 'a') as archivo:
        archivo.write(texto)
    print("Texto guardado:", texto)

# Función que se ejecuta cada 10 segundos
def guardar_periodicamente():
    while True:
        texto = input("Escribe algo ('fin' para terminar): ")
        if texto.lower() == 'fin':
            break  # Sal del bucle si se ingresa "fin"
        guardar_texto(texto + '\n')
        time.sleep(10)  # Espera 10 segundos antes de volver a pedir entrada

# Iniciar el hilo para guardar periódicamente
hilo = threading.Thread(target=guardar_periodicamente)
hilo.daemon = True  # El hilo se ejecutará en segundo plano
hilo.start()

try:
    # Mantén el programa principal en ejecución
    while hilo.is_alive():
        pass
    print("Programa finalizado.")
except KeyboardInterrupt:
    print("Programa finalizado.")
