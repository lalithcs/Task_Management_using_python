from authentication import user_registration, user_login
from file_organizer import user_interface

if __name__ == "__main__":
    while True:
        print("\nWelcome to File Organizer!")
        print("1. Register\n2. Login\n3. File Organizer\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_registration()
        elif choice == '2':
            if user_login():
                user_interface()  # If login successful, access file organizer
        elif choice == '3':
            user_interface()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
