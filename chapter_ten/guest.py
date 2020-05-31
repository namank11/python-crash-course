"""
 Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
"""

prompt = ''
file_name = 'supporting_files\guests.txt'
i = 1

while prompt != 'N' or prompt != 'n':
    prompt = input('Do you want to participate?(Y/N)')
    if prompt == 'n' or prompt == 'N':
        print('thanks')
        break
    else:
        name = input('Enter Your Name')
        with open(file_name, 'a') as file_object:
            file_object.write(f"{i}. {name}\n")
            i += 1

with open(file_name) as file_object:
    lines = file_object.read()
print(lines)
