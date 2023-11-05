import re
import sys

# Obtenemos el nombre de archivo de la plantilla
plantilla_html = sys.argv[1]


with open(plantilla_html) as archivo:
  contenido = archivo.read()

# Expresión regular para extraer desde inicio hasta </header>
header_regex = r'^(.*)</header>' 
header = re.search(header_regex, contenido, re.DOTALL).group()

header = re.sub(r'</title>(.*?)', r'</title>\n<?php wp_head(); ?>', header)


with open('header.php', 'w') as archivo:
  archivo.write(header)


print('Header actualizado correctamente')