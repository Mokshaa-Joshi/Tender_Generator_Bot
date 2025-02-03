import streamlit as st
from transformers import AutoTokenizer, AutoModel
import pinecone
from pdf_processing import extract_text_from_pdf, chunk_and_embed
from vector_store import init_pinecone, store_vectors_in_pinecone
from query_handler import query_to_vector, find_similar_chunk
from response_gen import generate_response

# Load Hugging Face model and tokenizer
model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize Pinecone
api_key = st.secrets["pinecone"]["api_key"]
index = init_pinecone(api_key)

# Streamlit UI
st.title("TenderBot")
uploaded_file = st.file_uploader("Upload your Tender PDF", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF and chunk it
    pdf_text = extract_text_from_pdf(uploaded_file)
    chunks, embeddings = chunk_and_embed(pdf_text, tokenizer, model)

    # Store vectors in Pinecone
    if st.button("Store PDF in Pinecone"):
        store_vectors_in_pinecone(index, chunks, embeddings)
        st.success("PDF stored in Pinecone.")

    # Query input
    query = st.text_input("Ask a question about the tender")
    
    if query:
        query_vector = query_to_vector(query, tokenizer, model)
        similar_chunk = find_similar_chunk(index, query_vector)
        answer = generate_response([similar_chunk], query)
        st.write(answer)
