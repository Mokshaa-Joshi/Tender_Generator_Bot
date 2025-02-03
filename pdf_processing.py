import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_and_embed(text, tokenizer, model, chunk_size=512):
    """Chunk the text into smaller pieces and convert to embeddings."""
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    embeddings = []

    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", truncation=True, padding=True)
        outputs = model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze()  # Average pooling
        embeddings.append(embedding.detach().cpu().numpy())

    return chunks, embeddings
