"""
 Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
 (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
"""

import time

start_time = time.time()
for i in range(1, 1000001):
    print(i)
end_time = time.time()
print(f'The Time taken to print from 1 to 1 million is {end_time-start_time} s')
