import csv

#The file name and header for the CSV file
FILE_NAME = "contacts.csv"
HEADER = ["Name", "Phone", "Email", "Favourite", "Speed Dial"]


# A function to read the contacts from the CSV file
def read_contacts():
    contacts = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

# A function to write the contacts to the CSV file
def write_contacts(contacts):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

# A function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    favourite = input("Is this a favourite contact? (y/n): ").lower() == "y"
    contacts = read_contacts()
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Favourite": favourite})
    write_contacts(contacts)
    print("Contact added successfully!")

# A function to edit an existing contact
def edit_contact():
    name = input("Enter name to edit: ")
    contacts = read_contacts()
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            favourite = input("Is this a favourite contact? (y/n): ").lower() == "y"
            contact["Phone"] = phone
            contact["Email"] = email
            contact["Favourite"] = favourite
            write_contacts(contacts)
            print("Contact updated successfully!")
            break
    else:
        print("Contact not found.")

# A function to search for a contact
def search_contact():
    search_term = input("Enter search term: ")
    contacts = read_contacts()
    found = False
    for contact in contacts:
        if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]:
            print(contact)
            found = True
    if not found:
        print("No contacts found.")

# A function to display favourite contacts
def display_favourites():
    contacts = read_contacts()
    favourites = [contact for contact in contacts if contact["Favourite"] == "True"]
    if favourites:
        for contact in favourites:
            print(contact)
    else:
        print("No favourite contacts found.")

# A function to add a speed dial
def add_speed_dial():
    name = input("Enter name to add to speed dial: ")
    contacts = read_contacts()
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            speed_dial = input("Enter speed dial number: ")
            contact["Speed Dial"] = speed_dial
            write_contacts(contacts)
            print("Speed dial added successfully!")
            break
    else:
        print("Contact not found.")

# A function to display speed dials
def display_speed_dials():
    contacts = read_contacts()
    speed_dials = [contact for contact in contacts if "Speed Dial" in contact]
    if speed_dials:
        for contact in speed_dials:
            print(contact["Name"], contact["Speed Dial"])
    else:
        print("No speed dials found.")
        
        
# Main function 

def main():
    while True:
        print("\n\nWelcome to the Contacts App!")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Search for a contact")
        print("4. Display favourite contacts")
        print("5. Add a speed dial")
        print("6. Display speed dials")
        print("7. Quit")
              
        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            display_favourites()
        elif choice == "5":
            add_speed_dial()
        elif choice == "6":
            display_speed_dials()
        elif choice == "7":
            print("Thank you for using Contacts App!")
            break

        else:
            print("Invalid choice. Please try again.")
            
            
main()



