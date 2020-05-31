"""
Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
•	Use a conditional test in the while statement to stop the loop.
•	Use an active variable to control how long the loop runs.
•	Use a break statement to exit the loop when the user enters a 'quit' value.
"""

print("Conditional Ending")
topping = ''
while topping != 'quit':
    topping = input("Enter the Topping You want to add to your pizza")
    if topping != 'quit':
        print(f"We will add {topping} topping to your pizza")
print("Active State")
topping = ''
flag = True
while (flag):
    topping = input("Enter the Topping You want to add to your pizza")
    if topping == 'quit':
        flag = False
    else:
        print(f"We will add {topping} topping to your pizza")
print("Break Statement")
topping = ''
while topping != 'quit':
    topping = input("Enter the Topping You want to add to your pizza")
    if topping == 'quit':
        break
    else:
        print(f"We will add {topping} topping to your pizza")
