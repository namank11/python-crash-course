"""
Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence, such as Reykjavik is in Iceland.
Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.
"""


def describe_cities(city, country='India'):
    print(f"{city.title()} is in {country.title()}")


describe_cities('agra')
describe_cities('ghaziabad')
describe_cities(country='USA', city='los angeles')
