"""
 Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the
 name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the
 whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip()
 , rstrip(), and strip().
"""

name_one = " naman\nkumar "
print(name_one.lstrip())
print(name_one.rstrip())
print(name_one.strip())

name_two = " naman\tkumar "
print(name_two.lstrip())
print(name_two.rstrip())
print(name_two.strip())
