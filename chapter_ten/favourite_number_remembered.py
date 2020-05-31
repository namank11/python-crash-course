"""
 Combine the two programs from Exercise 10-11 into one file. If the number is already stored,
 report the favorite number to the user.
 If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.
"""

import json

file_name = 'supporting_files/favourite_number_remembered.json'

try:
    with open(file_name) as file_object:
        favourite_number = json.load(file_object)
    print(f'I know your favourite number is {favourite_number}')

except FileNotFoundError:
    favourite_number = input('Enter you favourite number')
    with open(file_name, 'a') as file_object:
        json.dump(favourite_number, file_object)
    print(f'{favourite_number} is saved in {file_name}')
