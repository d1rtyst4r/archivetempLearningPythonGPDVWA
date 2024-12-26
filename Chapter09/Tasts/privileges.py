class Privileges():
    def __init__(self):
       self.privileges = ['add user', 'delete user', 'ban user']

    def get_privleges(self):
        """Print admin privileges to consol"""
        print("Admin has this privileges:")
        for privilege in self.privileges:
            print("\t" + privilege)

if __name__ == '__main__':
    my_privileges = Privileges()
    my_privileges.get_privleges() 