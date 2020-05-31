"""
 A Python dictionary can be used to model an actual dictionary.
 However, to avoid confusion, let’s call it a glossary.
 •	Think of five programming words you’ve learned about in the previous chapters.
 Use these words as the keys in your glossary, and store their meanings as values.
 •	Print each word and its meaning as neatly formatted output.
 You might print the word followed by a colon and then its meaning, or print the word on one line and then
 print its meaning indented on a second line. Use the newline character (\n) to insert a blank line
 between each word-meaning pair in your output.
"""

glossary = {'Fstring': 'specialized Formatted String, used when we want to print variables with string',
            'List': 'Data Type used to store any type of data and is mutable in nature',
            'Tuple': 'Tuple is not different from List but Tuples are immutable in nature',
            'Dictionary': 'These are the datatype which works on the concept of Key Value Pair',
            'Loops': 'These are used for looping through a centain number of steps based on some condition',
            }
for word, mean in glossary.items():
    print(f"{word} : - {mean}")
