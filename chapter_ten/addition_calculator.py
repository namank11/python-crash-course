"""
Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a
mistake and enter text instead of a number.
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
