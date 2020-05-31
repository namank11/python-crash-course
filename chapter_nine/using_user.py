"""
Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""

from chapter_nine.user import User

user1 = User('naman', 'kumar', '1234', 'ghaziabad')
user1.describe_user(User.user_details, 0)
user1.greet_user()

user2 = User('kumar', 'sambhav', '5678', 'gurugram')
user2.describe_user(User.user_details, 1)
user2.greet_user()
