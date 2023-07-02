import math
import os
import base64
from elasticsearch import Elasticsearch
import pandas as pd


# Configurar la conexión a Elasticsearch
es = Elasticsearch('http://localhost:9200')  # Actualiza con la configuración de tu instancia de Elasticsearch

# Directorio de origen de los archivos TXT
directorio_origen_txt = './../Procesado'  # Actualiza con la ruta correcta

# Directorio de origen de los archivos PDF
directorio_origen_pdf = './../PDF'  # Ruta del directorio de origen de los archivos PDF

# Directorio de origen del archivo Excel
directorio_origen_excel = './../Excel/Papers con informacion.xlsx'  # Ruta del archivo Excel


# Recorrer los archivos TXT y realizar la indexación
for archivo_txt in os.listdir(directorio_origen_txt):
    if archivo_txt.endswith('.txt'):
        # Obtener el nombre del archivo sin la extensión
        nombre_archivo = os.path.splitext(archivo_txt)[0]
        
        # Obtener el contenido del archivo TXT
        with open(os.path.join(directorio_origen_txt, archivo_txt), 'r', encoding='utf-8') as file:
            contenido = file.read()
        
        # Obtener el nombre del archivo PDF correspondiente
        archivo_pdf = f'{nombre_archivo.split("_")[0]}.pdf'  # Obtiene el nombre antes del guión bajo
        # Obtener el nombre del archivo correspondiente
        archivo_excel = f'{nombre_archivo.split("_")[0]}'  # Obtiene el nombre antes del guión bajo
        print('nombre archivo: ',archivo_excel)
        # Cargar el archivo Excel en un DataFrame
        df_excel = pd.read_excel(directorio_origen_excel)
        # Buscar el valor de archivo_excel en la columna "Nombre"
        filtro = df_excel['Nombre'] == archivo_excel
        fila_encontrada = df_excel[filtro].iloc[0]  # Obtener la primera fila que cumple con el filtro

        # Obtener los valores de las columnas requeridas y convertirlos a cadena de texto
        revista = str(fila_encontrada['Revista']) if 'Revista' in df_excel.columns else ""
        autores = str(fila_encontrada['Autor/es']) if 'Autor/es' in df_excel.columns else ""
        anio = int(fila_encontrada['Año']) if ('Año' in df_excel.columns and not math.isnan(fila_encontrada['Año'])) else 0
        abstract = str(fila_encontrada['Abstract']) if 'Abstract' in df_excel.columns else ""
        keywords = str(fila_encontrada['Keywords']) if 'Keywords' in df_excel.columns else ""
        idioma = str(fila_encontrada['Idioma']) if 'Idioma' in df_excel.columns else ""
        url = str(fila_encontrada['URL']) if 'URL' in df_excel.columns else ""

        # Verificar si el archivo PDF existe
        if not os.path.exists(os.path.join(directorio_origen_pdf, archivo_pdf)):
            print(f"No se encontró el archivo PDF correspondiente para '{archivo_txt}'. Continuando con la indexación.")
            continue
        
        # Leer el archivo PDF y convertirlo a base64
        with open(os.path.join(directorio_origen_pdf, archivo_pdf), 'rb') as file:
            contenido_pdf = file.read()
            contenido_pdf_base64 = base64.b64encode(contenido_pdf).decode('utf-8')
        
        # Crear el documento a indexar en Elasticsearch
        document = {
            'nombre': nombre_archivo,
            'contenido': contenido,
            'pdf_base64': contenido_pdf_base64,
            'revista': revista,
            'autores': autores,
            'abstract': abstract,
            'keywords': keywords,
            'idioma': idioma,
            'url': url
        }

        # Indexar el documento en Elasticsearch con un ID único basado en el nombre del archivo PDF
        index_name = "buscador"
        es.index(index=index_name, id=archivo_pdf, document=document)  # Actualiza con el nombre del índice adecuado
        print(f"Se ha indexado el archivo '{archivo_txt}' y su PDF correspondiente.")

print('Indexación completada')
