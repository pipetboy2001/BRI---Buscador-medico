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


# Cómo usar Elasticsearch
Para utilizar Elasticsearch en este proyecto, se asume que tienes una instancia de Elasticsearch en funcionamiento. Si aún no tienes Elasticsearch instalado y configurado, a continuación se muestran los pasos básicos para hacerlo:

Descarga Elasticsearch desde el sitio oficial: https://www.elastic.co/downloads/elasticsearch

Descomprime el archivo descargado en el directorio de tu elección.

Navega hasta el directorio de Elasticsearch y ejecuta el siguiente comando para iniciar el servidor:

```shell
./bin/elasticsearch
```

Verifica que Elasticsearch esté funcionando correctamente visitando http://localhost:9200 en tu navegador web. Deberías ver información sobre el clúster de Elasticsearch.

