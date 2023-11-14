import re
import pyperclip

phoneRegex = re.compile(r'''
                        (\d{3,4}|\(\d{3,4}\))?
                        (\s|-|\.)?
                        (\d{3,4})
                        (\s|-|\.)?
                        (\d{4})
                        ''', re.VERBOSE)

emailRegex = re.compile(r'''
                        (
                        [a-zA-Z0-9._%+-]+
                        @
                        ([a-zA-Z0-9.-]+
                        \.[a-zA-Z]{2,4})
                        )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('There is no phone number or e-mail address.')