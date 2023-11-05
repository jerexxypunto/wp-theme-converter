import sys
import os
from mover_files import move_file_to
from generate_basic_template import generate_css_theme
from generate_basic_assets import escribir_archivo, create_file

plantilla_html = sys.argv[1]
brand_name = sys.argv[2]
brand_slug = sys.argv[3]
author = sys.argv[4]
ruta_salida = sys.argv[5]

## genrar style.css
os.system('py generate_basic_assets.py')

## Separa el head
os.system(f'py separar_head.py {plantilla_html}')

## Separa el footer
os.system(f'py separar_footer.py {plantilla_html}')

## Separa el contenido
os.system(f'py separar_contenido.py {plantilla_html}')

## añado rutas compatibles con wordpress en el header.
os.system(f'py add_url_path.py header.php src assets')
os.system(f'py add_url_path.py header.php href assets')
os.system(f'py add_url_path.py header.php src vendor')
os.system(f'py add_url_path.py header.php href vendor')

## añado rutas compatibles con wordpress en el footer.
os.system(f'py add_url_path.py footer.php src assets')
os.system(f'py add_url_path.py footer.php href assets')
os.system(f'py add_url_path.py footer.php src vendor')
os.system(f'py add_url_path.py footer.php href vendor')

## añado rutas compatibles con wordpress en el contenido.
os.system(f'py add_url_path.py index.php src assets')
os.system(f'py add_url_path.py index.php href assets')
os.system(f'py add_url_path.py index.php src vendor')
os.system(f'py add_url_path.py index.php href vendor')

print("Se ha terminado de procesar la plantilla.")

create_file('./style.css')
escribir_archivo(f'./style.css', generate_css_theme(brand_name, brand_slug, author))

print("Se ha creado el fichero styles.css")

move_file_to('header.php', ruta_salida)
move_file_to('footer.php', ruta_salida)
move_file_to('index.php', ruta_salida)
move_file_to('style.css', ruta_salida)

print("Se han movido los archivos a la ruta de salida.")

