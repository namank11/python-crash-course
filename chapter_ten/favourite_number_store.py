"""
Write a program that prompts for the user’s favorite number.
Use json.dump() to store this number in a file. Write a separate program that reads in this value and
prints the message, “I know your favorite number! It’s _____.”
"""

import json

file_name = 'supporting_files/favourite_number.json'
favourite_number = input('Enter you favourite number')

with open(file_name, 'a') as file_object:
    json.dump(favourite_number, file_object)
print(f'{favourite_number} is saved in {file_name}')

