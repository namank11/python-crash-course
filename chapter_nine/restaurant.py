class Restaurant:
    '''A simple class for modeling a Restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''for initializing'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is an Awesome restaurant and has {self.cuisine_type.title()} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is Now Open")

    def set_number_served(self, customer_served):
        self.number_served = customer_served
        print(f"{self.number_served} No. of Customers have been served yet")

    def increment_number_served(self, customer_served):
        self.number_served = self.number_served + customer_served
        print(f"{self.number_served} have been served today")
