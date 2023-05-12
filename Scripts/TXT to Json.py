import json

# Leer el contenido del paper de texto plano
with open("paper.txt", "r") as f:
    content = f.read()

# Obtener el título y los autores del paper
title = ""
authors = []
for line in content.splitlines():
    if line.startswith("Title: "):
        title = line[7:].strip()
    elif line.startswith("Authors: "):
        authors = [author.strip() for author in line[9:].split(",")]

# Obtener el resumen del paper
abstract = content.split("Abstract: ")[1].split("\n\n")[0]

# Crear un objeto JSON que represente el contenido del paper
data = {
    "title": title,
    "authors": authors,
    "abstract": abstract,
    "content": content
}

# Convertir el objeto JSON a formato JSON y guardarlo en un archivo
with open("paper.json", "w") as f:
    json.dump(data, f)
