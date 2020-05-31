"""
An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or
Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better.
Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
"""


from chapter_nine.restaurant import Restaurant

class IceCreamStand(Restaurant):


    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours=['chocolate',
                       'vanilla',
                       'strawberry',
                       'litchi',
                       'mango']


    def display(self):
        for i in self.flavours:
            print(f"{i} is served in this stand")


ics1=IceCreamStand(restaurant_name='GayLords',cuisine_type='dessert')
if ics1.cuisine_type != 'dessert':
    print('Invalid Cuisine Type')
else:
    ics1.describe_restaurant()
    ics1.open_restaurant()
    ics1.set_number_served(10)
    ics1.increment_number_served(20)
    ics1.display()