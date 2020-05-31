"""
 Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs
 in the second file.
 Write a program that tries to read these files and print the contents of the file to the screen.
 Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message
 if a file is missing.
 Move one of the files to a different location on your system,
 and make sure the code in the except block executes properly.
"""

import os

file_cats = 'supporting_files\cats.txt'
file_dogs = 'supporting_files\dogs.txt'


def add_animal(file_name):
    name = input(f'Enter the name of the animal you want to enter in {file_name}')
    with open(file_name, 'a') as file_object:
        file_object.write(f'{name}\n')
        print(f'{name} has been written to {file_name}')


def view_animal(file_name):
    with open(file_name) as file_object:
        animal_name = file_object.readlines()
    for animal in animal_name:
        print(f'{animal}')


try:
    prompt_ask = input('What would you like to do today?'
                       '\nEnter 1 for adding more animals and '
                       '\n2 for viewing current animals')
    if prompt_ask == '1':
        prompt_animal = input('Which animal would you like to add?'
                              '\nEnter 1 for Dogs'
                              '\n2 for cats')
        if prompt_animal == '1':
            prompt_add_animal = ''
            while prompt_add_animal != 'quit':
                prompt_add_animal = input('Do you want to add animal?')
                if prompt_add_animal == 'quit':
                    print('Thanks for your response')
                else:
                    add_animal(file_dogs)
        elif prompt_animal == '2':
            prompt_add_animal = ''
            while prompt_add_animal != 'quit':
                prompt_add_animal = input('Do you want to add animal?')
                if prompt_add_animal == 'quit':
                    print('Thanks for your response')
                else:
                    add_animal(file_cats)
        else:
            print('you have entered a wrong choice ')
    elif prompt_ask == '2':
        prompt_animal = input('Which animal would you like to view?'
                              '\nEnter 1 for Dogs'
                              '\n2 for cats')
        if prompt_animal == '1':
            view_animal(file_dogs)
        elif prompt_animal == '2':
            view_animal(file_cats)
        else:
            print('you have entered a wrong choice ')
    else:
        print('You have entered a wrong choice')
except FileNotFoundError:
    print('The requested file not found')
