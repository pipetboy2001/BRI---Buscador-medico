import os
from openpyxl import Workbook

# Ruta de la carpeta que contiene los archivos PDF
carpeta_pdf = "./../PDF"

# Crear un libro de Excel
libro_excel = Workbook()
hoja_excel = libro_excel.active

# Escribir encabezados en las columnas
hoja_excel["A1"] = "Nombre"
hoja_excel["B1"] = "Revista"
hoja_excel["C1"] = "Autor/es"
hoja_excel["D1"] = "Año"
hoja_excel["E1"] = "Abstra"

# Obtener los nombres de los archivos PDF en la carpeta
archivos_pdf = [archivo for archivo in os.listdir(carpeta_pdf) if archivo.endswith(".pdf")]

# Rellenar la columna "Nombre" con los nombres de los archivos PDF sin la extensión
for indice, nombre_pdf in enumerate(archivos_pdf, start=2):
    nombre_sin_extension = os.path.splitext(nombre_pdf)[0]
    hoja_excel.cell(row=indice, column=1, value=nombre_sin_extension)

# Guardar el archivo Excel
libro_excel.save("archivo_excel.xlsx")
