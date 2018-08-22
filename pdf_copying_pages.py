
import PyPDF2

pdf_1_file = open('meetingminutes.pdf', 'rb')
pdf_2_file = open('meetingminutes2.pdf', 'rb')
pdf_1_reader = PyPDF2.PdfFileReader(pdf_1_file)
pdf_2_reader = PyPDF2.PdfFileReader(pdf_2_file)
pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(pdf_1_reader.numPages):
    page_obj = pdf_1_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

for page_num in range(pdf_2_reader.numPages):
    page_obj = pdf_2_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

pdf_output_file = open('combinedminutes.pdf', 'wb')
pdf_writer.write(pdf_output_file)
pdf_output_file.close()
pdf_1_file.close()
pdf_2_file.close()
