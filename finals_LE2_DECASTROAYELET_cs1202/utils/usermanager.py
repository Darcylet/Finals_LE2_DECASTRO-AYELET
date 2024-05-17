import os
from utils.user import User
class UserManager:
    def __init__(self, userfiles):
        self.users = {}
        self.load_users()
    
        
    def load_users(self):
        user_folder = 'users'
        user_file_path = os.path.join(user_folder, 'usersdata.txt')
    
        if os.path.exists(user_file_path):
            with open(user_file_path, 'r') as file:
                for line in file:
                    username, password = line.strip().split(', ' )
                    self.users[username] = User(username, password)
            

    def save_users(self):
        user_folder = 'users'
        user_file_path = os.path.join(user_folder, 'usersdata.txt')
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)
        with open(user_file_path, 'a') as file:
            for username, user in self.users.items():
                if username not in user_file_path:
                    file.write(f'{username}, {user.password}\n')

            

    def validate_username(self, username):
        if len(username) < 4:
            return False
        user_folder = 'users'
        user_file_path = os.path.join(user_folder, 'usersdata.txt')
        if os.path.exists(user_file_path):
            with open(user_file_path, 'r') as file:
                for line in file:
                    existing_username, _ = line.strip().split(', ')
                    if username == existing_username:
                        return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            return False
        return True

    def register(self, username, password):
        
        user = User(username, password)
        self.users[username] = user
        self.save_users()
        return True
        
    
    def login(self, username, password):
        if username not in self.users:
            print("\nUsername not found\n")
            return False
        user = self.users[username]
        if user.password != password:
            print("\nIncorrect password.\n")
            return False
        return True
    
