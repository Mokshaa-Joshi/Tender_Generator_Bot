import pinecone

def init_pinecone(api_key, index_name="tenderbot-index", dimension=768):
    """Initialize Pinecone and create the index."""
    pinecone.init(api_key=api_key)
    
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=dimension, metric="cosine")
    
    return pinecone.Index(index_name)

def store_vectors_in_pinecone(index, chunks, embeddings):
    """Store the embeddings and metadata in Pinecone."""
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        index.upsert([(str(i), embedding, {"chunk": chunk})])
