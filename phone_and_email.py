#! python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

# regex for phone numbers in format: 000-000-0000
# to be careful with number of brackets

# the "re.compile()" returns a REGEX object (regex pattern object)

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code, pipe '|' means to find either 123 or (123), '?' means not neccesary
    (\s|-|\.)?                          # match either whitespace | or hyphen | or dot or nothing at all = ?
    (\d{3})                             # first 3 digits, 123
    (\s|-|\.)                           # separator again
    (\d{4})                             # last 4 digits, 1234
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # any number of spaces followed by 'ext, x, or ext.', followed by 2 to 5 digits
    )''', re.VERBOSE)  # verbose flag allows to ignore whitespace and comments, to make it more readable

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # username, lowercase and uppercase letters, numbers or these symbols: ._%+-
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot-something, from 2-4 characters.
    )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard.')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

"""
Notes:

"-" is called hyphen
"|" is called pipe
"_" is called underline

"(wo)?" to match zero or just ONE instance = matches batman, batwoman, but not batwowowowoman
"(wo)*" to match ZERO or more instances = matches all of them - batman, matwoman, batwowowowoman...
"(wo)+" to match one or more instances = matches matwoman, batwowowowoman, but not batman

The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.

"?" is used also for declaring a nongreedy match
for example re.compile(r'(Ha){3,5}?') => HaHaHa, without "?" => HaHaHaHaHa

search() will return a match object (mo) of the first matched text
findall() method will return the strings of every match:
a list of strings if there are no groups... ['415-555-9999', '212-555-0000']
a list of tuples if there are groups ()()()... [('415', '555', '9999'), ('212', '555', '0000')]

\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.

[abc] matches any character between the brackets (such as a, b, or c)
[^abc] matches any character that isn’t between the brackets, with "^" caret symbol, which is used as well in:

(r'^Hello') to find strings starting with "Hello"
(r'\d$') to find strings ending with a digit 0-9

"." (or dot) character in a regular expression is called a wildcard and will match any character except for a newline

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') where ".*" means "anything" except a newline
to match all, the newline (\n) included, add "re.DOTALL"

re.compile(r'robocop', re.I) = regex case-insensitive

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
"CENSORED gave the secret documents to CENSORED."
"""



