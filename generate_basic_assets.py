import os

def escribir_archivo(filename, texto):
    
  # Comprobar si existe el directorio del archivo
  directorio = os.path.dirname(filename)
  if not os.path.exists(directorio):
    os.makedirs(directorio)

  # Abrir archivo para escritura
  f = open(filename, "w")

  # Escribir texto en el archivo
  f.write(texto)

  # Cerrar archivo
  f.close()

def create_file(filename):
    # Obtener el directorio actual 
    current_dir = os.getcwd()

    # Ruta completa del archivo
    file_path = os.path.join(current_dir, filename)

    # Crear el archivo vacío
    open(file_path, 'w').close()

    print(f'Archivo {filename} creado en {current_dir}')

    return filename


