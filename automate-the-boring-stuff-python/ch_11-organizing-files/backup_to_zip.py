'''
Requirements

Back up the entire contents of "folder" into a zip file
folder = Path(folder) Ensure the folder is a path object, not a string

Figure out the ZIP filename this code should use, based on what files already exist
'''

import zipfile, os, datetime
from pathlib import Path

def backup_to_zip(folder):
  number = 1
  while True:
    zip_filename = Path(folder.parts[-1] + '_' + str(number) + '.zip')
    print(zip_filename)
    if not zip_filename.exists():
      print(f'Found {zip_filename}')
      break
    number = number + 1

  # TODO: Create the ZIP file
  print(f'Creating {zip_filename}...')
  backup_zip = zipfile.ZipFile(zip_filename, 'w')

  # TODO: Walk the entire folder tree and compress the files in each folder.
  for folder_name, subfolders, filenames in os.walk(folder):
    folder_name = Path(folder_name)
    print(f'Adding files in folder {folder_name}...')

    # Add all the files in the folder to the ZIP file
    for filename in filenames:
      print(f'Adding file {filename}...')
      backup_zip.write(folder_name/filename)
  backup_zip.close()
  print('Done.')

backup_to_zip(Path.cwd()/'spam')
