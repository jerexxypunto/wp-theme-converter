import re
import sys

# Obtenemos el nombre de archivo de la plantilla
plantilla_html = sys.argv[1]
nav_regex = r'<nav.*(.*)</nav>'

with open(plantilla_html, 'r') as f:
    contenido = f.read()
    nav = re.search(nav_regex, contenido, re.DOTALL).group()

    ## Escribe fichero nav
    with open('nav.php', 'w') as archivo:
        archivo.write(nav)

new_html = re.sub(nav_regex, '<?php get_nav() ?>', contenido, flags=re.DOTALL)

with open(plantilla_html, 'w') as f:
    f.write(new_html)








# #with open(plantilla_html) as archivo:
# #  contenido = archivo.read()
#   ## Modificacontenido para reempalzar nav_regex por 'get_nav();'
# #  contenido = re.sub(nav_regex, '<?php get_nav(); ?>', contenido)



#print('nav creado correctamente')