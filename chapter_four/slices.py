"""
 Using one of the programs you wrote in this chapter, add several lines to the end of the program that
 do the following:
 •	Print the message The first three items in the list are:.
 Then use a slice to print the first three items from that program’s list.
 •	Print the message Three items from the middle of the list are:
 . Use a slice to print three items from the middle of the list.
 •	Print the message The last three items in the list are:
 . Use a slice to print the last three items in the list.
"""

list_cubes = [i ** 3 for i in range(1, 11)]
list_copy = list_cubes[:]
print(f"First Three Items in the list are:{list_copy[:4]}")
print(f"Middle Three Items in the list are:{list_copy[4:8]}")
print(f"First Three Items in the list are:{list_copy[-3:]}")
