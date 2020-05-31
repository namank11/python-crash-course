"""
 Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
 As they enter each topping, print a message saying you’ll add that topping to their pizza
"""

topping = ''
while (topping != 'quit'):
    topping = input("Enter the Topping You want to add to your pizza")
    if (topping != 'quit'):
        print(f"We will add {topping} topping to your pizza")
