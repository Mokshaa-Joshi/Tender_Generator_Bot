import numpy as np
from transformers import AutoTokenizer, AutoModel

def query_to_vector(query, tokenizer, model):
    """Convert the query to an embedding."""
    inputs = tokenizer(query, return_tensors="pt")
    outputs = model(**inputs)
    query_embedding = outputs.last_hidden_state.mean(dim=1).squeeze() 
    return query_embedding.detach().cpu().numpy()

def find_similar_chunk(index, query_vector, top_k=1):
    """Find the most similar chunk in Pinecone."""
    results = index.query([query_vector], top_k=top_k, include_metadata=True)
    return results["matches"][0]["metadata"]["chunk"]
