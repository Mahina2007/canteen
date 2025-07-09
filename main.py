from auth import register, login
def main():
    print("""
    1. Register
    2. Login
    3. Log out
    """)

    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            if register():
                print("registered successfully!")
            else:
                print("something went wrong, try again")
                register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Good bye")
            return None
        else:
            print("Invalid choice")
        return main()
    except KeyboardInterrupt:
        print("Good bye")
        return None

def user_menu():
    print("""
        1. Get a ticket
        2. Show my today time
        3. Show all my history
        """)
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        else:
            print("Invalid choice")
        return main()
    except KeyboardInterrupt:
        print("Good bye")
        return None

if __name__ == "__main__":
    main()