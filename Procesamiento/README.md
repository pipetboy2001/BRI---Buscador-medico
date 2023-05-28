# BRI - Buscador medico

## Requisitos

- Python 3.7 o superior

## Instalación

1. Clona o descarga este repositorio.

2. Navega hasta el directorio del proyecto.

Bibliotecas requeridas
A continuación se enumeran las bibliotecas requeridas para ejecutar este proyecto:

```shell
pip install PyPDF2
```

```shell
pip install nltk
```

Después de instalar nltk, ejecuta los siguientes comandos para descargar datos adicionales:

```shell
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
```

```shell
pip install elasticsearch
```

Recuerda que también puede haber dependencias adicionales que se instalan automáticamente si no están presentes en tu entorno.