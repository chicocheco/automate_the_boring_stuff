#! Python 3.6
# This file cannot be named 'trackback.py', otherwise it messes up with PyCharm!!!
# An exception can be caught and handled by the try and except statements.

import traceback

try:
    raise Exception('This is the error message.')
except:
    error_file = open('error_info.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written to error_info.txt.')
