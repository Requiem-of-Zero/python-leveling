'''
Requirements:

- Get a street address from the command line arguments or clipboard
- Opens the web browser to the OpenStreetMap page for that address

We need to:
Read the command line arguments from sys.argv
Read the clipboard contents
Call the webbrowser.open() to open the browser
Open a new file editor tab and save it as showmap.py
'''

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
  # Get address from command line
  address = " ".join(sys.argv[1:])
else:
# TODO: Get address from clipboard
  address = pyperclip.paste()

# TODO: Open the web browser
webbrowser.open('https://www.openstreetmap.org/search?query='+address)