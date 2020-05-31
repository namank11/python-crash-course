"""
Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made.
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
for sandwich in finished_sandwich:
    print(f'{sandwich.title()} is ready, Please come and collect your order')

