"""
One common problem when prompting for numerical input occurs when people provide text instead of numbers.
When you try to convert the input to an int, you’ll get a ValueError.
Write a program that prompts for two numbers. Add them together and print the result.
Catch the ValueError if either input value is not a number, and print a friendly error message.
Test your program by entering two numbers and then by entering some text instead of a number.
"""

message = ''
while message != 'quit':
    message = input('Do you want to add two numbers? No, type quit to close.')
    if message == 'quit':
        print('Thank you')
    else:
        try:
            number_one = int(input('Enter first number'))
            number_two = int(input('Enter second number'))
            addition = number_one + number_two
            print(f'The sum of the two values is {addition}')
        except ValueError:
            print('Please Enter only integers or float values')
