"""
Use the code in favorite_languages.py (page 97).
•	Make a list of people who should take the favorite languages poll.
Include some names that are already in the dictionary and some that are not.
•	Loop through the list of people who should take the poll.
If they have already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take the poll.
"""

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

for name, language in sorted(favorite_languages.items()):
    print(f"{name.title()} loves {language.title()}")

pollers = ['ram', 'jen', 'sarah', 'edward', 'phil', 'shyam']

for name in pollers:
    if (name in favorite_languages.keys()):
        print(f"{name} Thanks For Responding")
    else:
        print(f"{name} Please Vote!")
