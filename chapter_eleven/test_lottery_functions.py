"""
Building test cases for lottery_functions
"""

import unittest
from chapter_nine.lottery_functions import Lottery


class TestLotteryFunctionsMethods(unittest.TestCase):

    def test_check_winner(self):
        result = Lottery.check_winner([1,4,'e',0],[4,'e',0,1])
        self.assertEqual(result,True)


if __name__ == '__main__':
    unittest.main
