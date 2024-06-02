# HTML Template to WP Theme Converter


## Primer paso
Hacer git clone de este repo dentro de la carpeta de la plantilla HTML que se quiere convertir a theme de wordpress.

## Segudo paso
Ejecutar el comando `py main.py {fichero_index.html} "{Nombre del theme}" "{Slug del theme} ../"` en la carpeta del repo clonado.
<pre>
    cd wp-theme-converter
    py main.py ./fichero_index.html {Nombre del theme} {Slug del theme} {author} {ruta_salida} {css_path} {js_path}
</pre>
