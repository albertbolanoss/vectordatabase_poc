from pymilvus import model

# If connection to https://huggingface.co/ failed, uncomment the following path
# import os
# os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# This will download a small embedding model "paraphrase-albert-small-v2" (~50MB).
embedding_fn = model.DefaultEmbeddingFunction()


def convert_to_vectors(documents):
    vectors = embedding_fn.encode_documents(documents)

    return vectors

def encode_query(query):
    query_vectors = embedding_fn.encode_queries([query])

    return query_vectors