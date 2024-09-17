#!/usr/bin/env python3

import fitz

pdf_path = "src/medical_docs/sample1.pdf"
pdf_document = fitz.open(pdf_path)

for page_number in range(pdf_document.page_count):
    page = pdf_document.load_page(page_number)
    page_text = page.get_text("text")
    print(f"Page {page_number + 1}:\n{page_text}\n")

# Close the PDF file
pdf_document.close()