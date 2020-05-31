"""
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
You’ll have to think of someone else to invite.
•	Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name
of the guest who can’t make it.
•	Modify your list, replacing the name of the guest who can’t make it with the name of the new person
you are inviting.
•	Print a second set of invitation messages, one for each person who is still in your list.
"""

guests = ['ram', 'shyam', 'radha']
print(f'{guests[0].title()} you are invited.')
print(f'{guests[1].title()} you are invited.')
print(f'{guests[2].title()} you are invited.')
print(f'{guests[1].title()} will not be able to make it')
guests[1] = 'rohan'
print(f'{guests[1]} you are invited.')
print(f'{guests[0].title()} {guests[1].title()} {guests[2].title()} are Invited now.')
