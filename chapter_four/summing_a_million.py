"""
Make a list of the numbers from one to one million, and then use min() and max() to make sure your
list actually starts at one and ends at one million. Also, use the sum() function to see how quickly
Python can add a million numbers.
"""

import time

start_time = time.time()
sum = 0
for i in range(1, 1000001):
    print(i)
    sum += i
print(f'The sum of 1 to 1 million numbers is {sum}')
end_time = time.time()
print(f'The Time taken to sum from 1 to 1 million is {end_time-start_time} s')
