from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import matplotlib.pyplot as plt
import pandas as pd

def create_graph():
    data = {"Category": ["Labor", "Materials", "Transport"], "Cost": [50000, 75000, 25000]}
    df = pd.DataFrame(data)

    plt.figure(figsize=(4,3))
    plt.bar(df["Category"], df["Cost"], color=['blue', 'green', 'red'])
    plt.title("Budget Breakdown")
    plt.savefig("budget_graph.png")
    plt.close()

def generate_pdf(tender_content):
    pdf_path = "tender_document.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)
    
    # Add Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "Tender Proposal")
    
    # Add Text Content
    c.setFont("Helvetica", 12)
    text = c.beginText(100, 780)
    for line in tender_content.split("\n"):
        text.textLine(line)
    c.drawText(text)

    # Add Graph
    create_graph()
    c.drawImage("budget_graph.png", 150, 400, width=300, height=200)

    # Add Table
    data = [["Item", "Cost"], ["Labor", "$50,000"], ["Materials", "$75,000"], ["Transport", "$25,000"]]
    table = Table(data, colWidths=150, rowHeights=30)
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                               ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                               ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                               ("GRID", (0, 0), (-1, -1), 1, colors.black)]))
    
    table.wrapOn(c, 100, 100)
    table.drawOn(c, 100, 200)

    c.save()
    return pdf_path
