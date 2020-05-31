"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least
three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ['tuna sandwich',
                   'chicken sandwich',
                   'crispy sandwich',
                   'egg sandwich',
                   'pastrami sandwich'
    , 'pastrami sandwich'
    , 'pastrami sandwich']
finished_sandwich = []
while (len(sandwich_orders) != 0):
    sandwich_ready = sandwich_orders.pop()
    finished_sandwich.append(sandwich_ready)
print("Cafe has No Pastrami sandwich")
while ('pastrami sandwich' in finished_sandwich):
    finished_sandwich.remove('pastrami sandwich')
print("Ready to take Sandwiches")
for sandwich in finished_sandwich:
    print(sandwich)
