import os
import PyPDF2

# Obtiene la ruta completa del archivo PDF
pdf_path = os.path.abspath('./../Texts/Comparison.pdf')

# Abre el archivo PDF en modo binario
with open(pdf_path, 'rb') as f:
    # Lee el archivo PDF
    pdf = PyPDF2.PdfReader(f)
    text = ""

    # Itera sobre cada página del PDF
    for i in range(len(pdf.pages)):
        # Obtiene la página actual
        page = pdf.pages[i]

        # Obtiene el texto de la página y lo agrega a la variable text
        text += page.extract_text()


# Guarda el contenido en un archivo de texto plano
with open('paper.txt', 'w') as f:
    f.write(text)
