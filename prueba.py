def crear_pagina_html(titulo, contenido):
    # Definir la estructura básica del HTML
    html_contenido = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            color: #333;
        }}
        p {{
            color: #666;
        }}
    </style>
</head>
<body>
    <h1>{titulo}</h1>
    <p>{contenido}</p>
</body>
</html>
"""

    # Nombre del archivo
    nombre_archivo = "pagina.html"
    
    # Crear y escribir el archivo HTML
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(html_contenido)
    
    print(f"Archivo '{nombre_archivo}' creado exitosamente.")

# Leer entrada del usuario
titulo = input("Introduce el título de la página: ")
contenido = input("Introduce el contenido de la página: ")

# Crear la página HTML
crear_pagina_html(titulo, contenido)