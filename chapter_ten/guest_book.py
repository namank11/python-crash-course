"""
 Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen
 and add a line recording their visit in a file called guest_book.txt.
 Make sure each entry appears on a new line in the file.
"""

from time import time

prompt = ''
file_name = 'supporting_files\guest_book.txt'
i = 1

while prompt != 'N' or prompt != 'n':
    prompt = input('Do you want to Enter?(Y/N)')
    if prompt == 'n' or prompt == 'N':
        print('thanks')
        break
    else:
        name = input('Enter Your Name ')
        print(f'Welcome! {name} to the OldMonk Club')
        with open(file_name, 'a') as file_object:
            file_object.write(f"{i}. {name.title()} entered the club at {time()}\n")
            i += 1


with open(file_name) as file_object:
    lines = file_object.read()
print(lines)
