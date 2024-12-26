class User():
    def __init__(self, first_name : str, last_name : str, age : int):
        self.firtst_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(self.firtst_name.title() + " " + self.last_name.title() + " is " + str(self.age) + " years old.")
    
    def greet_user(self):
        print('Hello ' +  self.firtst_name.title() + " " + self.last_name.title() + ".")

    def increment_login_attempts(self):
        self.login_attempts +=1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def show_logins_attempts(self):
        print("This user has " + str(self.login_attempts) + " login attempts.")

ruslan = User('ruslan', 'jax', 18)
robert = User("robert", 'baratheon', 48)
ted = User('ted', 'govard', 36)
if __name__ == '__main__':
    ruslan.describe_user()
    ruslan.greet_user()
    robert.describe_user()
    robert.greet_user()
    ted.describe_user()
    ted.greet_user()
    ted.increment_login_attempts()
    ted.increment_login_attempts()
    ted.show_logins_attempts()
    ted.reset_login_attempts()
    ted.show_logins_attempts()
