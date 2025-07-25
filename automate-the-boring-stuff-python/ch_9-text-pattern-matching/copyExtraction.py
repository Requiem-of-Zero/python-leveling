'''
Requirements:

- Get the text from the clipboard
- Find all phone numbers and email addresses in the text.
  - Create two regex patterns, one for the phone numbers and one for emails
  - Find all matches (not just the first match)
- Paste them onto the clipboard
  - pyperclip to copy and paste strings
- Neatly format the matched strings into a single string to paste
- Display some kind of message if no matches were found in the text

'''

import pyperclip, re

phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

# TODO: Create email regex

email_re = re.compile(r'''(
                      [a-zA-Z0-9._%+-]+ # Username
                      @ # @ symbol
                      [a-zA-Z0-9.-]+ # Domain name
                      (\.[a-zA-Z]{2,4}) # Dot-something
                      )''', re.VERBOSE)

# emailSearch1 = re.search(email_re, "theesamwong@gmail.com")
# phoneSearch1 = re.search(phone_re, "123-415-2313")

# TODO: Find matches in clipboard text

clipboard_text = str(pyperclip.paste())

matches = []

print(phone_re.findall(clipboard_text))

for groups in phone_re.findall(clipboard_text):
  phone_num = '-'.join([groups[1], groups[3], groups[5]])
  if groups[6] != '':
    phone_num += ' x' + groups[6]
  matches.append(phone_num)

for groups in email_re.findall(clipboard_text):
  matches.append(groups[0])

print(matches)
# TODO: Copy results to the clipboard

if len(matches) > 0:
  match_str = '\n'.join(matches)
  pyperclip.copy(match_str)
  print('Copied to clipboard:')
  print(match_str)
else:
  print("No phone numbers or email addresses found.")
  
# print(phoneSearch1)
# print(emailSearch1)