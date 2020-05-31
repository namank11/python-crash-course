"""
 Use a dictionary to store information about a person you know.
 Store their first name, last name, age, and the city in which they live.
 You should have keys such as first_name, last_name, age, and city.
 Print each piece of information stored in your dictionary.
"""

person = {}
last_name = input("Enter Last Name")
first_name = input("Enter First Name")
age = input("Enter Age")
city = input("Enter City")
person['lastname'] = last_name
person['firstname'] = first_name
person['age'] = age
person['city'] = city
print(person)
