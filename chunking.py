import PyPDF2
from sentence_transformers import SentenceTransformer

# Initialize model for embedding
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def chunk_text(text, chunk_size=500):
    chunks = []
    words = text.split(' ')
    for i in range(0, len(words), chunk_size):
        chunks.append(' '.join(words[i:i+chunk_size]))
    return chunks

def embed_text(text_chunks):
    return model.encode(text_chunks)
