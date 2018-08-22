
import PyPDF2

minutes_file = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(minutes_file)
minutes_first_page = pdf_reader.getPage(0)

pdf_watermark_reader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

# Merge the first page of one PDF with the first page of another PDF.
minutes_first_page.mergePage(pdf_watermark_reader.getPage(0))


# Create an empty PDF writer object where to add the page with the watermark.
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(minutes_first_page)
# Now add everything from the second page up to the end.
for page_num in range(1, pdf_reader.numPages):
    page_obj = pdf_reader.getPage(page_num)     # Read it.
    pdf_writer.addPage(page_obj)                # Write it.

# Open a new PDF in 'wb' mode where to save the content of PDF writer object.
result_pdf_file = open('watermarked_cover.pdf', 'wb')
pdf_writer.write(result_pdf_file)

minutes_file.close()
result_pdf_file.close()
