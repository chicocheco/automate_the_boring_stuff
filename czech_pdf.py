
import pdftotext

with open('record-statement-contact-ABERNAU') as f:
    pdf = pdftotext.PDF(f)

print(pdf)


