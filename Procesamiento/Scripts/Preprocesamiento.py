import os
import re
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ruta de la carpeta con los archivos de texto de entrada
carpeta_origen = './../TXT'

# Ruta de la carpeta de destino para los archivos procesados
carpeta_destino = './../Procesado'

# Crear la carpeta de destino si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Obtener la lista de archivos en la carpeta de origen
archivos_txt = os.listdir(carpeta_origen)

# Inicializar el lematizador de NLTK
lemmatizer = WordNetLemmatizer()

# Definir las stopwords en el idioma adecuado
stopwords = set(stopwords.words('english'))  # Utiliza los stopwords en inglés
# Iterar sobre cada archivo en la carpeta de origen
for archivo_txt in archivos_txt:
    # Verificar si el archivo es un archivo de texto
    if archivo_txt.endswith('.txt'):
        # Ruta completa del archivo de texto de entrada
        ruta_txt_entrada = os.path.join(carpeta_origen, archivo_txt)

        # Leer el contenido del archivo de texto
        with open(ruta_txt_entrada, 'r', encoding='utf-8') as f:
            contenido = f.read()

        # Realizar el procesamiento del texto
        # Eliminación de caracteres no deseados
        contenido = re.sub(r'[^\w\s]', '', contenido)

        # Tokenización
        tokens = word_tokenize(contenido)

        # Eliminación de stopwords y lematización
        tokens_procesados = [lemmatizer.lemmatize(token) for token in tokens if token.lower() not in stopwords]

        # Unir los tokens procesados en un texto nuevamente
        texto_procesado = ' '.join(tokens_procesados)

        # Ruta completa del archivo de texto procesado de salida
        archivo_procesado = archivo_txt[:-4] + '_procesado.txt'
        ruta_txt_salida = os.path.join(carpeta_destino, archivo_procesado)

        # Guardar el contenido procesado en un archivo de texto plano
        with open(ruta_txt_salida, 'w', encoding='utf-8') as f:
            f.write(texto_procesado)

        print(f'Se ha procesado "{archivo_txt}" y se ha guardado en "{ruta_txt_salida}"')
