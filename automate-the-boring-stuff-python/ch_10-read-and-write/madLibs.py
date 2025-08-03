'''
Requirements:

Create Mad Libs program that reads in text files and lets the user add their
own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

Example text file:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurences and prompt the user to replace them

Example output text file:
The silly panda walked to the chandelier and then screamed. A nearby
pickup truck was unaffected by these events.
'''

import re # For finding placeholder words
import sys
from pathlib import Path # For file handling

# TODO: Load input file
input_path = Path(sys.argv[1])

if not input_path.exists():
  print('Input file not found.')
  exit()

with input_path.open('r', encoding='UTF-8') as file:
  content = file.read()

# TODO: Define the regex pattern for placeholders
madlibs_pattern = re.compile(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b')

# TODO: Replace each placeholder with user input
def prompt_word(word_type):
  article = 'an' if word_type[0] in 'AEIOU' else 'a'
  return input(f'Enter {article} {word_type.lower()}: ')

# Go through each match and prompt
output = content
for match in madlibs_pattern.findall(content):
  replacement = prompt_word(match)
  output = output.replace(match, replacement, 1)

# TODO: Write to a new file
output_path = Path(input_path).resolve().parent/Path('madlibs_output.txt')
with output_path.open('w', encoding='UTF-8') as out_file:
  out_file.write(output)

print(f'\nMad Libs completed. Output saved to: {output_path}')
print(output)