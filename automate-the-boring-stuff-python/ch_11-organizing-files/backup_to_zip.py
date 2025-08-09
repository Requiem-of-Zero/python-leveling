'''
Requirements

Back up the entire contents of "folder" into a zip file
folder = Path(folder) Ensure the folder is a path object, not a string

Figure out the ZIP filename this code should use, based on what files already exist
'''

import zipfile, os
from pathlib import Path

def backup_to_zip(folder):
  print(folder)