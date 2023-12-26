from data import file_details  # Importing the file_details dictionary from data.py

# Assuming file_details contains dictionary entries with details like {'file_name': {'file_type': 'txt', 'file_size': 1024, 'date_modified': '2023-01-01'}}
# Implement the sorting logic based on criteria

def sort_files(file_list, criteria):
    if criteria == 'file_type':
        return sorted(file_list, key=lambda x: file_details[x]['file_type'])
    elif criteria == 'file_size':
        return sorted(file_list, key=lambda x: file_details[x]['file_size'])
    elif criteria == 'date_modified':
        return sorted(file_list, key=lambda x: file_details[x]['date_modified'])
    else:
        return file_list

def add_file(filename, details):
    file_details[filename] = details

def retrieve_file(filename):
    return file_details.get(filename, "File not found")

def user_interface():
    print("Welcome to File Organizer!")
    while True:
        print("\n1. Sort Files\n2. Display Files\n3. Retrieve File Details\n4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            criteria = input("Sort files by (file_type, file_size, date_modified): ")
            sorted_files = sort_files(file_details.keys(), criteria)
            print("Files sorted:")
            for file_name in sorted_files:
                details = file_details[file_name]
                print(f"File: {file_name}, Type: {details.get('file_type', 'N/A')}, Size: {details.get('file_size', 'N/A')}KB, Date Modified: {details.get('date_modified', 'N/A')}")
        elif choice == '2':
            print("Displaying files:")
            for file_name, details in file_details.items():
                print(f"File: {file_name}, Type: {details.get('file_type', 'N/A')}, Size: {details.get('file_size', 'N/A')}KB, Date Modified: {details.get('date_modified', 'N/A')}")
        elif choice == '3':
            file_name = input("Enter file name to retrieve details: ")
            details = retrieve_file(file_name)
            if details != "File not found":
                print(f"File: {file_name}, Type: {details.get('file_type', 'N/A')}, Size: {details.get('file_size', 'N/A')}KB, Date Modified: {details.get('date_modified', 'N/A')}")
            else:
                print("File not found.")
        elif choice == '4':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Try again.")
