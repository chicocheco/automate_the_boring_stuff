
import PyPDF2

# Open the file with 'rb' argument (read-binary).
minutes_file = open('meetingminutes.pdf', 'rb')
# Create a PDF reader object by passing the opened file.
pdf_reader = PyPDF2.PdfFileReader(minutes_file)

# Create a page object.
page = pdf_reader.getPage(0)
page.rotateClockwise(90)

# Create a PDF writer object with no argument, empty.
pdf_writer = PyPDF2.PdfFileWriter()
# Add the page to the PDF writer object.
pdf_writer.addPage(page)

# Open another, second file with 'wb' argument (write-binary).
result_pdf_file = open('rotatedPage.pdf', 'wb')
# Write the content of the pdf writer object, using the .write method, to the created pdf file.
pdf_writer.write(result_pdf_file)

result_pdf_file.close()
minutes_file.close()
