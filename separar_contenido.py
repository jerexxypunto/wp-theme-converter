import re
import sys

plantilla_html = sys.argv[1]
output_format = sys.argv[2]

if(len(output_format) == 0):
  output_format = 'index.php'
   


with open(plantilla_html) as archivo:
  contenido = archivo.read()

# Expresión regular para contenido principal
content_regex = r'</header>(.*)<footer>'

# Extraemos el contenido principal 
content = re.search(content_regex, contenido, re.DOTALL).group()


# Agregamos llamadas a header y footer
content = re.sub(r'^(.*)</header>' , '<?php get_header(); ?>', content)
content = re.sub(r'<footer.*?(.*)', '<?php get_footer(); ?>', content)

# Guardamos en index.php
with open(output_format, 'w') as archivo:
  archivo.write(content)

# Reemplazamos en la plantilla  
contenido = re.sub(content_regex, '<?php get_content(); ?>', contenido)

with open(plantilla_html, 'w') as archivo:
  archivo.write(contenido)

print(f'{output_format} generado')