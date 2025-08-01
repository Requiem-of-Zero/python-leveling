'''
We're a geography teacher with 35 students in our class and want to give a pop quiz
on US state capitals. Unfortunately, our class has a few bad eggs in it, and you can't
trust the students not to cheat. You'd like to randomize the order of questions so
that each quiz is unique, making it impossible for anyone to crib answers from anyone else

Requirements:

* Creates 35 different quizzes
* Creates 50 multiple-choice questions for each quiz, in random order
* Provides the correct answer and three random wrong answers for each question, in random order
* Writes the quizzes to 35 text files
* Writes the answer keys to 35 text files
* Store the states and their capitals in a dictionary
* Call open(), write(), and close() for the quiz and answer key text files
* Use random.shuffle() to randomize the order of the questions and multiple-choice options
'''

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
 'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# TODO: Generate 35 quiz files.
for quiz_num in range(35):
  # TODO: Create the quiz and answer key files.

  # TODO: Write out the header for the quiz

  # TODO: Shuffle the order of the states.

  # TODO: Loop through all 50 states, making a question for each.