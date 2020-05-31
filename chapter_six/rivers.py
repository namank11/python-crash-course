"""
Make a dictionary containing three major rivers and the country each river runs through.
One key-value pair might be 'nile': 'egypt'.
•	Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
•	Use a loop to print the name of each river included in the dictionary.
•	Use a loop to print the name of each country included in the dictionary
"""

rivers = {'kosi': 'dadyal', 'ganga': 'haridwar', 'yamuna': 'delhi', 'hindon': 'ghaziabad'}
for river, place in rivers.items():
    print(f"{river} flows through {place}")
for river in rivers.keys():
    print(f"{river} is present in dictionary")
for place in rivers.values():
    print(f"{place} is present in dictionary")
