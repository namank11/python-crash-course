"""
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
"""

from chapter_nine.restaurant import Restaurant

restaurant2 = Restaurant('sagar', 'punjabi')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3 = Restaurant('sami', 'odiya')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
