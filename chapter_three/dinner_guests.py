"""
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for
only two guests.
•	Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite
only two people for dinner.
•	Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time
you pop a name from your list, print a message to that person letting them know you’re sorry you can’t
invite them to dinner.
•	Print a message to each of the two people still on your list, letting them know they’re still invited.
•	Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.
"""

guests = ['ram', 'shyam', 'radha']
print(f"{guests[0].title()} you are invited.")
print(f"{guests[1].title()} you are invited.")
print(f"{guests[2].title()} you are invited.")
print(f"{guests[1].title()} will not be able to make it")
guests[1] = 'rohan'
print(f"{guests[1].title()} you are invited.")
guests.insert(0, 'sita')
guests.insert(1, 'geeta')
guests.append('babita')
print(f'{guests[0].title()}'
      f' {guests[1].title()}'
      f' {guests[2].title()}'
      f' {guests[3].title()}'
      f' {guests[4].title()}'
      f' {guests[5].title()}'
      f' are Invited now.')
print("Sorry, for the Inconvienence the bigger table is not available now."
      "So we have to drop some guests")
for i in guests:
    while len(guests) > 2:
        guest_out = guests.pop()
        print(f"{guest_out.title()} your invitation has been revoked")
print(f"{guests[0].title()} you are still invited")
print(f"{guests[1].title()} you are still invited")
print(f'{len(guests)} are Invited only Now.')
