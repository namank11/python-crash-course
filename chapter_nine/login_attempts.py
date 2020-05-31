"""
Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
Write a method called increment_login _attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.
"""

from chapter_nine.user import User
user1=User('naman','kumar','1234','ghaziabad')
users={}
u_id=0
user1.describe_user(users,u_id)
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()