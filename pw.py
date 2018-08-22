#! python3
# pw.py - An insecure password locker program.

import sys
import pyperclip

PASSWORDS = {'email': 'heslonaemail123',
             'blog': 'hesloproblog9873278',
             'luggage': '1234'}

if len(sys.argv) < 2:  # at least one argument to pass is a must
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

""" The first argument, sys.argv[0], is always the name of the program as it was invoked, 
and sys.argv[1] is the first argument you pass to the program."""

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
