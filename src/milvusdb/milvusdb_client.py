from pymilvus import MilvusClient

client = MilvusClient(host='localhost', port='19530')


def create_collection_or_truncate(collection_name):
    if client.has_collection(collection_name=collection_name):
        client.drop_collection(collection_name=collection_name)
    
    client.create_collection(
        collection_name=collection_name,
        dimension=768,  # The vectors we will use in this demo has 768 dimensions
    )

def insert_vectors(collection_name, vectors):
    res = client.insert(collection_name=collection_name, data=vectors)

    return res

def search(collection_name, search_vectors, limit, subject):
    res = client.search(
        collection_name=collection_name,
        data=search_vectors,
        filter=f"subject == '{subject}'",
        limit=limit,
        output_fields=["text", "subject"],
    )

    return res

