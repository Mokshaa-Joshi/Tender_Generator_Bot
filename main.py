import openai
import streamlit as st
from fpdf import FPDF
import os
from dotenv import load_dotenv

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate the tender document using OpenAI API
def generate_tender_content(data):
    prompt = f"""
    Generate a detailed tender document based on the following input:

    1. General Information:
    - Title & Reference Number: {data['title_reference']}
    - Issuing Organization: {data['issuing_organization']}
    - Type of Procurement: {data['procurement_type']}
    - Deadline for Submission: {data['submission_deadline']}
    - Contact Information: {data['contact_info']}

    2. Project Scope & Requirements:
    - Project Description: {data['project_description']}
    - Scope of Work: {data['scope_of_work']}
    - Technical Specifications: {data['technical_specs']}
    - Expected Outcomes: {data['expected_outcomes']}

    3. Budget & Pricing Structure:
    - Estimated Budget: {data['estimated_budget']}
    - Payment Terms: {data['payment_terms']}
    - Pricing Format: {data['pricing_format']}

    4. Submission Guidelines:
    - Proposal Format: {data['proposal_format']}
    - Required Documents: {data['required_documents']}
    - Submission Method: {data['submission_method']}

    5. Evaluation Criteria:
    - Selection Process: {data['selection_process']}
    - Scoring Criteria: {data['scoring_criteria']}
    - Eligibility Requirements: {data['eligibility_requirements']}

    6. Terms & Conditions:
    - Contract Duration: {data['contract_duration']}
    - Legal Obligations: {data['legal_obligations']}
    - Confidentiality & Intellectual Property: {data['confidentiality_ip']}
    - Termination Clause: {data['termination_clause']}

    The output should be formatted as a formal, well-structured tender document. Make sure the language is clear, professional, and easy to read.
    """
    
    # Updated API call using GPT-4 chat model
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Using GPT-4 chat model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,  # Adjust based on your document length
        temperature=0.7
    )

    return response['choices'][0]['message']['content']


# Function to create a PDF from generated tender content
def create_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    return pdf

# HTML and CSS styling
def add_custom_styles():
    st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f6f8;
        color: #333;
    }

    .title {
        color: #4CAF50;
        text-align: center;
        font-size: 36px;
        margin-bottom: 40px;
    }

    .form-section {
        margin-bottom: 30px;
    }

    .form-section label {
        font-size: 16px;
        color: #555;
    }

    .submit-button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border: none;
        padding: 12px 20px;
        cursor: pointer;
        border-radius: 5px;
    }

    .submit-button:hover {
        background-color: #45a049;
    }

    .download-btn {
        background-color: #007bff;
        color: white;
        font-size: 18px;
        padding: 12px 20px;
        border: none;
        cursor: pointer;
        border-radius: 5px;
    }

    .download-btn:hover {
        background-color: #0056b3;
    }

    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: white;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
    }

    .content-header {
        font-size: 24px;
        color: #333;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit App layout
add_custom_styles()

st.markdown('<div class="title">Tender Generator Bot</div>', unsafe_allow_html=True)

st.sidebar.header("Tender Information")

# General Information Input
st.sidebar.subheader("1. General Information")
title_reference = st.sidebar.text_input("Title & Reference Number")
issuing_organization = st.sidebar.text_input("Issuing Organization")
procurement_type = st.sidebar.selectbox("Type of Procurement", ["Goods", "Services", "Works"])
submission_deadline = st.sidebar.date_input("Deadline for Submission")
contact_info = st.sidebar.text_input("Contact Information (Procurement Officer)")

# Project Scope & Requirements Input
st.sidebar.subheader("2. Project Scope & Requirements")
project_description = st.sidebar.text_area("Project Description")
scope_of_work = st.sidebar.text_area("Scope of Work")
technical_specs = st.sidebar.text_area("Technical Specifications")
expected_outcomes = st.sidebar.text_area("Expected Outcomes")

# Budget & Pricing Structure Input
st.sidebar.subheader("3. Budget & Pricing Structure")
estimated_budget = st.sidebar.text_input("Estimated Budget (if disclosed)")
payment_terms = st.sidebar.text_input("Payment Terms")
pricing_format = st.sidebar.selectbox("Pricing Format", ["Lump sum", "Hourly rate", "Per unit"])

# Submission Guidelines Input
st.sidebar.subheader("4. Submission Guidelines")
proposal_format = st.sidebar.text_area("Proposal Format")
required_documents = st.sidebar.text_area("Required Documents")
submission_method = st.sidebar.text_input("Submission Method")

# Evaluation Criteria Input
st.sidebar.subheader("5. Evaluation Criteria")
selection_process = st.sidebar.text_area("Selection Process")
scoring_criteria = st.sidebar.text_area("Scoring Criteria")
eligibility_requirements = st.sidebar.text_area("Eligibility Requirements")

# Terms & Conditions Input
st.sidebar.subheader("6. Terms & Conditions")
contract_duration = st.sidebar.text_input("Contract Duration")
legal_obligations = st.sidebar.text_area("Legal Obligations")
confidentiality_ip = st.sidebar.text_area("Confidentiality & Intellectual Property")
termination_clause = st.sidebar.text_area("Termination Clause")

# Button to generate the tender
if st.sidebar.button("Generate Tender Document"):
    # Collect all data into a dictionary
    data = {
        "title_reference": title_reference,
        "issuing_organization": issuing_organization,
        "procurement_type": procurement_type,
        "submission_deadline": submission_deadline,
        "contact_info": contact_info,
        "project_description": project_description,
        "scope_of_work": scope_of_work,
        "technical_specs": technical_specs,
        "expected_outcomes": expected_outcomes,
        "estimated_budget": estimated_budget,
        "payment_terms": payment_terms,
        "pricing_format": pricing_format,
        "proposal_format": proposal_format,
        "required_documents": required_documents,
        "submission_method": submission_method,
        "selection_process": selection_process,
        "scoring_criteria": scoring_criteria,
        "eligibility_requirements": eligibility_requirements,
        "contract_duration": contract_duration,
        "legal_obligations": legal_obligations,
        "confidentiality_ip": confidentiality_ip,
        "termination_clause": termination_clause
    }

    # Generate tender document content using OpenAI
    tender_content = generate_tender_content(data)

    # Display generated tender content
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.subheader("Generated Tender Document")
    st.text_area("Tender Content", tender_content, height=300)
    st.markdown('</div>', unsafe_allow_html=True)

    # Create PDF of the tender
    pdf = create_pdf(tender_content)

    # Save the generated PDF file
    tender_pdf_path = "generated_tender.pdf"
    pdf.output(tender_pdf_path)

    # Provide a download button for the PDF
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.download_button(
        label="Download Tender Document as PDF",
        data=open(tender_pdf_path, "rb").read(),
        file_name="Tender_Document.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
