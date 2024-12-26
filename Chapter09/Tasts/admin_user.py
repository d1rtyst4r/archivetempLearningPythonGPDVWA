from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

if __name__ == '__main__':
    admin = Admin('Jon', 'Dow', 24)
    admin.privileges.get_privleges()