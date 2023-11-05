import re
import sys
from urllib.parse import urlparse

plantilla_html = sys.argv[1]
brand_name = sys.argv[2]
ruta_salida = sys.argv[3]

with open(plantilla_html) as archivo:
  contenido = archivo.read()

# Expresiones regulares para CSS y JS
css_regex = r'<link .*href="([^"]+.css)"'  
js_regex = r'<script .*src="([^"]+.js)"'

css_files = re.findall(css_regex, contenido)
js_files = re.findall(js_regex, contenido)

# Función para generar la ruta de WordPress
def wp_path(url):
  return url

# Generamos el código de functions.php
enqueue_css = "\n".join([f"wp_enqueue_style( 'theme', get_template_directory_uri() . '{wp_path(css)}');" for css in css_files])
enqueue_js = "\n".join([f"wp_enqueue_script( 'theme', get_template_directory_uri() . '{wp_path(js)}');" for js in js_files])

output = f"""
<?php
function {brand_name}_enqueue() {{

{enqueue_css}

{enqueue_js}

}}
add_action( 'wp_enqueue_scripts', 'theme_enqueue' );
?>
"""

# Guardamos functions.php
with open('functions.php', 'w') as archivo:
  archivo.write(output)
  
print('functions.php actualizado')