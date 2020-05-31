"""
 Add an if test to hello_admin.py to make sure the list of users is not empty.
 •	If the list is empty, print the message We need to find some users!
 •	Remove all of the usernames from your list, and make sure the correct message is printed.
"""

users = ['manager']
if not users:
    print('We need to find some more users')
else:
    for user in users:
        if (user == 'admin'):
            print(f"{user}, would you like to see a satus report")
        else:
            print(f"{user}, Thanks for logging in Again.")
