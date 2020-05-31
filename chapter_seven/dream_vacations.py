"""
Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where would you go?
Include a block of code that prints the results of the poll.
"""

dream_places = {}
message = ''
while (message != 'quit'):
    message = input("Would You Like to participate in Polling")
    if (message == 'quit'):
        break
    else:
        name = input("Enter you name")
        place = input("Enter the place you want to visit")
        dream_places[name] = place
for name, place in dream_places.items():
    print(f"{name} wants to visit {place} one day")
