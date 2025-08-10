'''
Requirements

Automate these steps:
- Right-click a link in a web browser
- Select the Copy Link or Copy Link Address item from the context menu
- Switch to the spreadsheet app
- Press CTRL-V to paste the link
- Switch back to the web browser

Needs to be automated because it is tedious when a page has dozen or hundreds of links. 
We can create a small clipboard-recording program to make it faster.
The program will monitor the clipboard to see if new text has been copied to it, and if so, it will print it to the terminal screen

We can convert our five-step process into two steps:
- Right-click a link in a web browser
- Select the Copy Link or Copy Link Address item from the context menu
'''

import pyperclip, time

print('Recording clipboard... (Ctrl-C to stop)')
seen = set()
try:
  while True:
    content = pyperclip.paste() # Get clipboard content

    if content not in seen: # If different from the previous, print it
      print(content)
      seen.add(content)
    time.sleep(0.01) # Pause to avoid hogging CPU
except KeyboardInterrupt:
  pass