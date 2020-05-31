"""
Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
•	Add a new pizza to the original list.
•	Add a different pizza to the list friend_pizzas.
•	Prove that you have two separate lists. Print the message My favorite pizzas are:,
and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:,
and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
"""

my_pizzas = ['pepperoni', 'chicken dominator', 'cheese burst']
friend_pizzas = my_pizzas[:]
my_pizzas.append('thin crust')
print('My favourite pizzas are: ')
for pizza in my_pizzas:
    print(pizza.title())
friend_pizzas.append('margherita')
print('My friends favourite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza.title())
