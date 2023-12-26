from authentication import user_registration, user_login, add_password, retrieve_and_validate_password
from file_organizer import user_interface

if __name__ == "__main__":
    while True:
        print("\nWelcome to File Organizer!")
        print("1. Register\n2. Login\n3. File Organizer\n4. Add Password\n5. Retrieve Password\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_registration()
        elif choice == '2':
            if user_login():
                user_interface()  # If login successful, access file organizer
        elif choice == '3':
            user_interface()
        elif choice == '4':
            add_password()
        elif choice == '5':
            retrieve_and_validate_password()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
