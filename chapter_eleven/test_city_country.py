"""
Write a function that accepts two parameters: a city name and a country name.
The function should return a single string of the form City, Country, such as Santiago, Chile.
Store the function in a module called city_functions.py. Create a file called test_cities.py that tests
the function you just wrote (remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function with values such as
'santiago' and 'chile' results in the correct string. Run test_cities.py, and make sure test_city_country() passes.
"""

import unittest
from chapter_eleven.city_country import city_country
from chapter_eleven.city_country_population import city_country_population


class TestCityCountry(unittest.TestCase):
    def test_city_country_method(self):
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_population_method(self):
        result = city_country_population('santiago', 'chile','700000')
        self.assertEqual(result, 'Santiago, Chile - population 700000')

    def test_city_country_population_method_optional(self):
        result = city_country_population('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main
