# Contact Manager Program

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    email = input("Enter contact email: ").strip()
    mobile = input("Enter contact mobile number: ").strip()
    contacts[name] = {"email": email, "mobile": mobile}
    print(f"Contact {name} added successfully.")

def view_contact():
    name = input("Enter the name of the contact you want to view: ").strip()
    if name in contacts:
        print(f"Name: {name}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Mobile: {contacts[name]['mobile']}")
    else:
        print("Contact not found.")

def edit_contact():
    name = input("Enter the name of the contact you want to edit: ").strip()
    if name in contacts:
        print("1. Edit email")
        print("2. Edit mobile number")
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == '1':
            new_email = input("Enter the new email: ").strip()
            contacts[name]['email'] = new_email
            print(f"Email updated for {name}.")
        elif choice == '2':
            new_mobile = input("Enter the new mobile number: ").strip()
            contacts[name]['mobile'] = new_mobile
            print(f"Mobile number updated for {name}.")
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def view_all_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("All contacts:")
    for name, info in contacts.items():
        print(f"Name: {name}, Email: {info['email']}, Mobile: {info['mobile']}")

def menu():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            view_all_contacts()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the program
menu()
