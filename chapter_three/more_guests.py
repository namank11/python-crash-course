"""
You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
•	Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program
informing people that you found a bigger dinner table.
•	Use insert() to add one new guest to the beginning of your list.
•	Use insert() to add one new guest to the middle of your list.
•	Use append() to add one new guest to the end of your list.
•	Print a new set of invitation messages, one for each person in your list.
"""

guests = ['ram', 'shyam', 'radha']
print(f"{guests[0].title()} you are invited.")
print(f"{guests[1].title()} you are invited.")
print(f"{guests[2].title()} you are invited.")
print(f"{guests[1].title()} will not be able to make it")
guests[1] = 'rohan'
print(f"{guests[1].title()} you are invited.")
print(f'{guests[0].title()} {guests[1].title()} {guests[2].title()} are Invited now.')
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
