import re
import sys

plantilla_html = sys.argv[1]
find = sys.argv[2]
findType = sys.argv[3]

def replace_href_in_file(contenido, findType):
  # Expresiones regulares
    pattern1 = fr'(href="{findType})'
    repl = fr'href="<?php echo get_template_directory_uri(); ?>/{findType}'
    contenido = re.sub(pattern1, repl, contenido)
    return contenido

def replace_src_in_file(contenido, findType):
  # Expresiones regulares
    pattern = fr'(src="{findType})'
    repl = fr'src="<?php echo get_template_directory_uri(); ?>/{findType}'
    contenido = re.sub(pattern, repl, contenido)
    return contenido





with open(plantilla_html) as archivo:
  contenido = archivo.read()

  if(find == "href"):
    contenido = replace_href_in_file(contenido, findType)

if(find == "src"):
    contenido = replace_src_in_file(contenido, findType)



with open(plantilla_html, 'w') as archivo:
  archivo.write(contenido)  

