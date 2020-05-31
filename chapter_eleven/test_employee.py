import unittest
from chapter_eleven.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee('naman', 'kumar', '150000')

    def test_give_default_raise(self):
        result = self.emp1.give_raise()
        self.assertEqual(result, 155000)

    def test_give_custom_raise(self):
        result = self.emp1.give_raise(50000)
        self.assertEqual(result, 200000)


if __name__ == '__main__':
    unittest.main
