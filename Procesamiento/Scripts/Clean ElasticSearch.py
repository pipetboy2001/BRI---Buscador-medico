from elasticsearch import Elasticsearch

# Configurar la conexión a Elasticsearch
es = Elasticsearch('http://localhost:9200')  # Actualiza con la configuración de tu instancia de Elasticsearch

# Nombre del índice que deseas eliminar todo su contenido
index_name = "buscador"  # Actualiza con el nombre de tu índice

# Realizar una búsqueda para verificar si hay documentos en el índice
search_results = es.search(index=index_name, body={"query": {"match_all": {}}}, scroll='5m')

# Obtener el número de documentos encontrados
total_docs = search_results["hits"]["total"]["value"]

if total_docs > 0:
    # Si hay documentos, construir la consulta para eliminar todos los documentos del índice
    query = {
        "query": {
            "match_all": {}
        }
    }

    # Ejecutar la eliminación por consulta en el índice
    response = es.delete_by_query(index=index_name, body=query, scroll='5m')

    # Verificar si la eliminación fue exitosa
    if response["deleted"]:
        print(f"Se eliminaron {response['deleted']} documentos del índice {index_name}.")
    else:
        print("No se encontraron documentos para eliminar.")
else:
    print("El índice está vacío. No se encontraron documentos para eliminar.")
