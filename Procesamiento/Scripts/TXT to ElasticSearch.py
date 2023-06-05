import os
import base64
from elasticsearch import Elasticsearch

# Configurar la conexión a Elasticsearch
es = Elasticsearch('http://localhost:9200')  # Actualiza con la configuración de tu instancia de Elasticsearch

# Directorio de origen de los archivos TXT
directorio_origen_txt = './../TXT'  # Ruta del directorio de origen de los archivos TXT

# Recorrer los archivos TXT y realizar la indexación
for archivo_txt in os.listdir(directorio_origen_txt):
    if archivo_txt.endswith('.txt'):
        # Obtener el nombre del archivo sin la extensión
        nombre_archivo = os.path.splitext(archivo_txt)[0]
        
        # Obtener el contenido del archivo TXT
        with open(os.path.join(directorio_origen_txt, archivo_txt), 'r', encoding='utf-8') as file:
            contenido = file.read()
        
        # Codificar el contenido en base64
        contenido_base64 = base64.b64encode(contenido.encode('utf-8')).decode('utf-8')
        
        # Crear el documento a indexar en Elasticsearch
        document = {
            'nombre': nombre_archivo,
            'contenido': contenido_base64
        }

        # Indexar el documento en Elasticsearch con un ID único basado en el nombre del archivo TXT
        index_name = "buscador"
        es.index(index=index_name, id=nombre_archivo, document=document)  # Actualiza con el nombre del índice adecuado
        print(f"Se ha indexado el archivo '{archivo_txt}'.")

print('Indexación completada')
