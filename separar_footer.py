import re
import sys

plantilla_html = sys.argv[1]


with open(plantilla_html) as archivo:
  contenido = archivo.read()

# Expresión regular para extraer el footer  
footer_regex = r'<footer.*?(.*)'

# Extraemos el footer
footer = re.search(footer_regex, contenido, re.DOTALL).group()

## modificamos contenido para que despues de la etiqueta </footer> en la siguiente linea se agregue la llamada a <?php wp_footer(); ?>.
footer = re.sub(r'</footer>(.*?)', r'</footer>\n<?php wp_footer(); ?>', footer)

# Guardamos el footer en un archivo 
with open('footer.php', 'w') as archivo:
  archivo.write(footer)  



print('Footer separado correctamente')