"""
Start with a copy of user_profile.py from page 149.
Build a profile of yourself by calling build_profile(),
using your first and last names and three other key-value pairs that describe you.
"""


def build_profile(first_name, last_name, **personality):
    for key, value in personality.items():
        print(f"{first_name}{last_name} has {value}{key}")


build_profile(first_name='ram', last_name='sharma', strength='great', personality='vibrant')
