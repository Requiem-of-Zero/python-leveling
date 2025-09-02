'''
Requirements:
  - Load the XKCD home page
  - Save the comic image on that page
  - Follow the Previous Comic link.
  - Repeat until it reaches the first comic or the max download limit

Needs to do following:
  - Download pages with the requests module
  - Find the URL ofthe comic image for a page using Beautiful Soup
  - Download and save the comic image to the hard drive with iter_content()
  - Find the URL of the Previous Comic Link, and repeat
'''