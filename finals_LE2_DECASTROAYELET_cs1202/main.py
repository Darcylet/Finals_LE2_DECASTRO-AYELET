from utils.usermanager import UserManager
from utils.dicegame import Dicegame
import os


def main():
    user_manager = UserManager('usersdata.txt')

    try:
        while True:
            print("\nWelcome to Dice Game!\n")
            print("1. Register")
            print("2. Log in")
            print("3. Exit\n")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                os.system('cls')
                print("CREATE AN ACCOUNT")
                username = input("\nCreate a username(at least 4 characters): ")
                if not user_manager.validate_username(username):
                    print("Username taken or invalid number of characters")
                    continue

                password = input("Create a password(at least 8 characters): ")

                if not user_manager.validate_password(password):
                    print("password should be atleast 8 characters")
                    continue
                if user_manager.register(username, password):
                    print("Successfully Registered")
                    print(f'Welcome {username}!')


            elif choice == 2:
                os.system('cls')
                print("LOG IN")
                username = input("\nEnter username: ")
                password = input("Enter password: ")
                if user_manager.login(username, password):
                    print("Log in successful")
                    game = Dicegame(username)
                    if not game.menu(username):
                        continue

            elif choice == 3:
                quit()


            else:
                print("\n\nINVALID INPUT. please try again.")
                continue
    except ValueError:
        print("Invalid input")
        


if __name__ == "__main__":
    main()
