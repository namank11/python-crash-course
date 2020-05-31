"""
 An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote
 in Exercise 9-3 (page 162) or Exercise 9-5 (page 167).
 Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user",
 and so on. Write a method called show_privileges() that lists the administrator’s set of privileges.
 Create an instance of Admin, and call your method.
"""
from chapter_nine.user import User


class Admin(User):
    def __init__(self, fname, lname, upass, uadd):
        super().__init__(fname, lname, upass, uadd)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"{self.fname.title()} {self.lname.title()} ")
        for i in self.privileges:
            print(f"{i}")


usr1 = Admin('naman', 'kumar', '1234', 'bengaluru')
usr1.show_privileges()
