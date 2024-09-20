#!/usr/bin/env python3
from utils.summary_report.summary_extractor import SummaryReportExtractor
from utils.detailed_report.detailed_extractor import DetailedReportExtractor
import fitz

# Define the path to the PDF file
pdf_path = "src/medical_docs/sample1.pdf"

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Extract text from the PDF
text = ""
for page_number in range(pdf_document.page_count):
    page = pdf_document.load_page(page_number)
    text += page.get_text("text")


# Close the PDF file
pdf_document.close()

summary_extractor = SummaryReportExtractor(text=text)
detailed_extractor = DetailedReportExtractor(text=text)
summary_extractor.generate_dataframe()
detailed_extractor.generate_dataframe()
# extractor.convert_column_types()

print(summary_extractor.summary_report_df)
print(detailed_extractor.detailed_report_df)
