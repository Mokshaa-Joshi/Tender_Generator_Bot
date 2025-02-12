import streamlit as st
from generate_tender import generate_tender
from pdf_generator import generate_pdf

st.title("TenderBot - AI-Powered Tender Generation")

query = st.text_input("Enter keywords for your tender:")

if st.button("Generate Tender"):
    if query:
        with st.spinner("Generating Tender..."):
            tender_text = generate_tender(query)
            pdf_path = generate_pdf(tender_text)
            st.success("Tender generated successfully!")

            with open(pdf_path, "rb") as f:
                st.download_button("Download Tender PDF", f, file_name="Tender_Document.pdf", mime="application/pdf")
    else:
        st.error("Please enter keywords for tender generation.")
