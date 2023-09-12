import threading
import os
from io import BytesIO
from PIL import Image

# Directorio de entrada y salida
input_dir = "imagenes"
output_dir = "imagenes_procesadas"

# Crear la carpeta de salida si no existe
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Función para cargar una imagen, invertir colores y guardarla
def procesar_imagen(filename):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)
    
    print(f"Procesando imagen: {filename}")
    
    try:
        # Cargar la imagen
        with open(input_path, 'rb') as file:
            image_data = file.read()
        
        image = Image.open(BytesIO(image_data))
        
        # Invertir los colores de la imagen
        inverted_image = Image.new("RGB", image.size)
        inverted_pixels = [(255 - r, 255 - g, 255 - b) for (r, g, b) in image.getdata()]
        inverted_image.putdata(inverted_pixels)
        
        # Guardar la imagen procesada
        with open(output_path, 'wb') as file:
            inverted_image.save(file, format="PNG")
        
        print(f"Imagen procesada y guardada en: {output_path}")
    except Exception as e:
        print(f"Error al procesar la imagen {filename}: {str(e)}")

# Lista de archivos en la carpeta de entrada
image_files = os.listdir(input_dir)

# Creamos un hilo para procesar cada imagen
threads = []
for filename in image_files:
    thread = threading.Thread(target=procesar_imagen, args=(filename,))
    threads.append(thread)
    thread.start()

# Esperamos a que todos los hilos terminen
for thread in threads:
    thread.join()

print("Procesamiento de imágenes completado.")
