'''
Requirements

- Get search keywords from the command line arguments
  - Read the command line arguments from sys.argv
- Retrieve the search results page
  - Fetch the search results page with the requests module
- Open a browser tab for each result
  - Call the webbrowser.open() function to open the web browser
'''

import requests, sys, webbrowser, bs4

print('Searching...') # Display text while downloading the search results page.
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search results links

# TODO: Open a browser tab for each result.