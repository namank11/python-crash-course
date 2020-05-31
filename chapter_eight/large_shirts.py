"""
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""


def design_tshirts(message, size='large'):
    print(f"{size.title()} sized Shirt with '{message.title()}' printed will be delivered..")


design_tshirts('i love java')
