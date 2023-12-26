from hashlib import sha256
from data import file_details  # Importing the file_details dictionary from data.py

user_credentials = {'user1': 'password1'}  # Example initial user

def save_credentials(username, password):
    hashed_password = sha256(password.encode()).hexdigest()
    user_credentials[username] = hashed_password

def check_credentials(username, password):
    stored_password = user_credentials.get(username)
    if stored_password:
        hashed_password = sha256(password.encode()).hexdigest()
        return stored_password == hashed_password
    return False

def save_password(filename, password):
    encrypted_password = sha256(password.encode()).hexdigest()
    file_details[filename] = {'password': encrypted_password}

def retrieve_password(filename, entered_password):
    stored_password = file_details.get(filename, {}).get('password')
    if stored_password:
        entered_password = sha256(entered_password.encode()).hexdigest()
        return stored_password == entered_password
    return False

def user_registration():
    print("Register a new account")
    username = input("Enter username: ")
    password = input("Enter password: ")
    save_credentials(username, password)
    print("Registration successful!")

def user_login():
    print("Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if check_credentials(username, password):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def add_password():
    filename = input("Enter filename: ")
    password = input("Enter password: ")
    save_password(filename, password)
    print("Password saved!")

def retrieve_and_validate_password():
    filename = input("Enter filename: ")
    entered_password = input("Enter password: ")
    if retrieve_password(filename, entered_password):
        print("Password correct!")
    else:
        print("Incorrect password or file doesn't exist.")
