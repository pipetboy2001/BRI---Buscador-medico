import base64
# pip install elasticsearch
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

with open('./../Texts/Comparison.pdf', 'rb') as file:
    pdf_content = file.read()
    base64_content = base64.b64encode(pdf_content).decode('utf-8')

document = {
    "attachment": base64_content
}

index_name = "my_index"
document_id = "1"

es.index(index=index_name, id=document_id, document=document)
print("Documento indexado correctamente en Elasticsearch.")
