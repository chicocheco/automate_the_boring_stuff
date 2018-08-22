# Logging is better than using 'print()' because it can be disabled\activated with a single line of code

import logging

#  logging.disable(logging.CRITICAL) to disable logging!!!
logging.basicConfig(filename='my_program_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %('
                                                                               'message)s')
logging.debug('Start of program')


def factorial(n):
    logging.debug(f'Start of factorial({n})')
    total = 1
    for i in range(1, n + 1):  # range(6) iterates from 0 to 5, 6 not included!... FIXED to 1 - 5, because 0*1 is 0
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug(f'End of factorial({n})')
    return total


print(factorial(5))  # 5*4*3*2*1 = 120
logging.debug('End of program')

"""
before fixing:

2015-05-23 16:20:12,664 - DEBUG - Start of program
2015-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
2015-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
2015-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
2015-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
2015-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
2015-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
2015-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
2015-05-23 16:20:12,680 - DEBUG - End of factorial(5)
0
2015-05-23 16:20:12,684 - DEBUG - End of program
"""

"""
There are five logging levels and it is up to the programer to decide how to use them.
Later it is posible to show only important messages like 'level=logging.ERROR'

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
"""
