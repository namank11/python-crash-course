class User:
    user_details = {}
    u_id = 0

    def __init__(self, fname, lname, upass, uadd):
        self.fname = fname
        self.lname = lname
        self.upass = upass
        self.uadd = uadd
        self.login_attempts = 0

    def describe_user(self, user_details, u_id):
        individual_user = {'first_name': self.fname, 'last_name': self.lname, 'user_pass': self.upass,
                           'user_add': self.uadd}
        self.user_details[u_id] = individual_user
        print(self.user_details)
        self.u_id += 1

    def greet_user(self):
        print(f"Welcome! {self.fname} {self.lname}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.login_attempts} times Logged in!!")
