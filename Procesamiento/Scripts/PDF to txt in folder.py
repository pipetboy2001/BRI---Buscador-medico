import os
import PyPDF2

# Ruta de la carpeta con los archivos PDF de entrada
carpeta_origen = './../PDF'

# Ruta de la carpeta de destino para los archivos de texto convertidos
carpeta_destino = './../TXT'

# Obtener la lista de archivos en la carpeta de origen
archivos_pdf = os.listdir(carpeta_origen)

# Iterar sobre cada archivo en la carpeta de origen
for archivo_pdf in archivos_pdf:
    # Verificar si el archivo es un PDF
    if archivo_pdf.endswith('.pdf'):
        # Ruta completa del archivo PDF de entrada
        ruta_pdf = os.path.join(carpeta_origen, archivo_pdf)

        # Abrir el archivo PDF en modo binario
        with open(ruta_pdf, 'rb') as f:
            # Leer el archivo PDF
            pdf = PyPDF2.PdfReader(f)
            text = ''

            # Iterar sobre cada página del PDF
            for page in pdf.pages:
                # Extraer el texto de la página y agregarlo a la variable 'text'
                text += page.extract_text()

        # Ruta completa del archivo de texto de salida
        archivo_txt = archivo_pdf[:-4] + '.txt'  # Cambiar la extensión a .txt
        ruta_txt = os.path.join(carpeta_destino, archivo_txt)

        # Guardar el contenido en un archivo de texto plano
        with open(ruta_txt, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f'Se ha convertido "{archivo_pdf}" a texto y se ha guardado en "{ruta_txt}"')
