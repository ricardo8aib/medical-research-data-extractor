import fitz

# Define the path to the PDF file
pdf_path = "src/medical_docs/med_sample_2.pdf"

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Extract text from the PDF
text = ""
for page_number in range(pdf_document.page_count):
    page = pdf_document.load_page(page_number)
    text += page.get_text("text")

print(text[0:500])

pdf_document.close()
