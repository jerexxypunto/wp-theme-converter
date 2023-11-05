import shutil

## Una función que mueve archivos de un directorio a otro
def move_file_to(file, directory):
    try:
        shutil.move(file, directory)
    except:
        print("No se pudo mover el archivo " + file + " al directorio " + directory)