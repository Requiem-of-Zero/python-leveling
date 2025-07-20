'''
consonant - letters that represent certain speech sounds, sounds that involve blocking the air before it leaves the mouth
consonants: bcdfghjklmnpqrstvwxyz
vowels: aeiou
- Begins with a vowel, the word yay is added to the end of it.
- if a word begins with a consonant or consonant cluster like (ch or gr), that consonant or consonant cluster is moved to the end of the word and followed by ay

Enter the English message to translate into pig latin:
My name is AL SWEIGART and I am 4,000 years old.
Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.
'''

def convert_to_piglatin():
  print('Enter the English message to translate: ')
  message = input()

  vowels = 'aeiouy'
  consonants = 'bcdfghjklmnpqrstvwxyz'
  pig_latin = [] # a list of the words in pig latin

  for word in message.split():
    # Separate the non-letters at the start of this word:
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
      prefix_non_letters += word[0]
      word = word[1:]
    if len(word) == 0:
      pig_latin.append(prefix_non_letters)
      continue
    
    # Separate the non-letters at the end of this word:
    suffix_non_letters = ''
    while not word[-1].isalpha():
      suffix_non_letters = word[-1] + suffix_non_letters
      word = word[:1]

    # Remember if the word was in uppercase or title case:
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower() # Make the word lowercase for translation

    # Separate the consonants at the start of this word:
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in vowels:
      prefix_consonants += word[0]
      word = word[1:]
    
    # Add the pig latin ending to the word:
    if prefix_consonants != '':
      word += prefix_consonants + 'ay'
    else:
      word += 'yay'

    # Set the word back to uppercase or title case:
    if was_upper:
      word = word.upper()
    if was_title:
      word = word.title()

    # Add the non-letters back to the start or end of the word.
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)
  
  # Join all the words back together into a single string:
  print(" ".join(pig_latin))

convert_to_piglatin()