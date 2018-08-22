
import PyPDF2

pdf_file = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

pdf_writer = PyPDF2.PdfFileWriter()

# Copy the PDF page by page.
for page_num in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(page_num))

# Encrypt the newly created PDF with the password 'swordfish'.
pdf_writer.encrypt('swordfish')

result_pdf = open('encryptedminutes.pdf', 'wb')
pdf_writer.write(result_pdf)

result_pdf.close()

"""
PDFs can have a user password (allowing you to view the PDF) and an owner password 
(allowing you to set permissions for printing, commenting, extracting text, and other features). 
The user password and owner password are the first and second arguments to encrypt(), respectively. 
If only one string argument is passed to encrypt(), it will be used for both passwords.
"""