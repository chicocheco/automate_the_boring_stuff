#! python3

import docx


def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    # Return one long string of joined separate paragraphs with '\n' so each paragraph starts on a new line.
    return '\n'.join(full_text)


print(get_text('demo.docx'))

