#! python3
# pdf_pass_breaker.py - Searches over 88,000 uppercase and lowercase words from the dictionary
#                       to find a password of an encrypted PDF file.


import PyPDF2

pdf_filename = input('Enter the name of your PDF file in the CWD (e.g. "encrypted.pdf"):\n')

raw_dict = open('dictionary.txt', 'r')
words_capital = raw_dict.read().splitlines()
words_lower = [word.lower() for word in words_capital]
words = words_lower + words_capital

pdf_file = open(pdf_filename, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

for word in words:
    print(word)
    if pdf_reader.decrypt(word) == 1:
        print(f'The password for the pdf "{pdf_filename}" is "{word}".')
        break

raw_dict.close()
