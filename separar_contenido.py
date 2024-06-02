import re
import sys

plantilla_html = sys.argv[1] if len(sys.argv) > 1 else None
output_format = sys.argv[2] if len(sys.argv) > 2 else 'index.php'


with open(plantilla_html) as archivo:
  contenido = archivo.read()

# Expresión regular para contenido principal
content_regex = r'</header>(.*)<footer>'



# Extraemos el contenido principal 
content_1 = re.split(r'</header>', contenido, maxsplit=1)[1]

# Extraemos todo lo que está antes de la cadena <footer>
content_1 = re.split(r'<footer', content_1, maxsplit=1)[0]


# Agregamos llamadas a header y footer
content = '<?php get_header(); ?> \r' + content_1 + '\r<?php get_footer(); ?>'

# Guardamos en index.php
with open(output_format, 'w') as archivo:
  archivo.write(content)

# Reemplazamos en la plantilla  
#contenido = re.sub(content_regex, '<?php get_content(); ?>', contenido)

# with open(plantilla_html, 'w') as archivo:
#   archivo.write(contenido)

print(f'{output_format} generado')