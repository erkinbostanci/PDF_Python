# Pip Install #
#pip install PyPDF2


# IMPORT #
import PyPDF2


# Reading PDFs #
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
# Page Number
pdf_reader.numPages
# Select Page
page_one = pdf_reader.getPage(0)
# Extract Text In Pdf
page_one_text = page_one.extractText()
print(page_one_text)
f.close()


# Adding to PDFs #
f = open('Working_Business_Proposal.pdf','rb')
# Read
pdf_reader = PyPDF2.PdfFileReader(f)
#Page Number
first_page = pdf_reader.getPage(0)
# Write
pdf_writer = PyPDF2.PdfFileWriter()
# Add Page
pdf_writer.addPage(first_page)
# Open Other Pdf
pdf_output = open("Some_New_Doc.pdf","wb")
# Write Other Pdf
pdf_writer.write(pdf_output)
f.close()


# Simple Example #
f = open('Working_Business_Proposal.pdf','rb')

# Create Page List
pdf_text = []
# Read
pdf_reader = PyPDF2.PdfFileReader(f)
#Num Page in pdf_reader
for p in range(pdf_reader.numPages):
    # Get Page Number
    page = pdf_reader.getPage(p)
    # Append List
    pdf_text.append(page.extractText())
# 4. Page Get
print(pdf_text[3])