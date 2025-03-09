
'''
      
            Name : Antuley Aman Siraj
            Roll No : 23CO25
            Batch - 01


                *Mini-Project*
            Topic : Contact Book

'''




contacts = {}  

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added successfully!\n")

def update_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(f"Contact {name} updated successfully!\n")
    else:
        print(f"Contact {name} not found!\n")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}\n")
    else:
        print(f"Contact {name} not found!\n")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!\n")
    else:
        print(f"Contact {name} not found!\n")

def display_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("Contact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()

while True:
    print("\n Contact Book Menu")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    
    elif choice == "2":
        name = input("Enter contact name to update: ")
        new_phone = input("Enter new phone number: ")
        update_contact(name, new_phone)
    
    elif choice == "3":
        name = input("Enter contact name to search: ")
        search_contact(name)
    
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    
    elif choice == "5":
        display_contacts()
    
    elif choice == "6":
        print("Exiting Contact Book.....")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 6.\n")


# Conclusion : 