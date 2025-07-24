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

phone_re = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
email_re = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

emailSearch1 = re.search(email_re, "theesamwong@gmail.com")
phoneSearch1 = re.search(phone_re, "123-415-2313")

print(emailSearch1)