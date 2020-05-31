import json

file_name = 'supporting_files/favourite_number.json'

with open(file_name) as file_object:
    favourite_number = json.load(file_object)
print(f'I know your favourite number is {favourite_number}')
