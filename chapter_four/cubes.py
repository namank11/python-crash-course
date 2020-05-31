"""
A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
and use a for loop to print out the value of each cube
"""

list_cubes = []
for number in range(1, 11):
    cubes = number ** 3
    list_cubes.append(cubes)
print(list_cubes)
