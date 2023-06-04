import os
from elasticsearch import Elasticsearch

# Configurar la conexión a Elasticsearch
es = Elasticsearch('http://localhost:9200')  # Actualiza con la configuración de tu instancia de Elasticsearch

# Directorio de origen de los archivos TXT simples
directorio_origen_txt = './../TXT'  # Actualiza con la ruta correcta

# Recorrer los archivos TXT y realizar la indexación
for archivo_txt in os.listdir(directorio_origen_txt):
    if archivo_txt.endswith('.txt'):
        # Obtener el nombre del archivo sin la extensión
        nombre_archivo = os.path.splitext(archivo_txt)[0]
        
        # Obtener el contenido del archivo TXT
        with open(os.path.join(directorio_origen_txt, archivo_txt), 'r', encoding='utf-8') as file:
            contenido = file.read()
        
        # Crear el documento a indexar en Elasticsearch
        document = {
            'nombre': nombre_archivo,
            'contenido': contenido
        }

        # Indexar el documento en Elasticsearch con un ID único basado en el nombre del archivo TXT
        index_name = "buscador"
        es.index(index=index_name, id=archivo_txt, document=document)  # Actualiza con el nombre del índice adecuado
        print(f"Se ha indexado el archivo '{archivo_txt}'.")

print('Indexación completada')
