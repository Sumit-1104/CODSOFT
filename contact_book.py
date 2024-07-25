#python project for contact Book.
#Requirement for project
    #1. name of the contact book
    #2. phone number of contact book
    #3. Email of contact book
    #4. Address of contact book

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
     
    def view_contact(self):
        if not self.contacts:
            print("No contact in the book.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone:{contact.phone_number}, Email:{contact.email}, Address:{contact.address}")

    def search_contact(self,search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts
     
    def update_contact(self, contact_name, new_contact):
        for contact in self.contacts:
            if contact.name == contact_name:
                contact.name == new_contact
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address

    def deleted_contact(self, contact_name):
        self.contacts = [contact for contact in self.contacts if contact.name != contact_name]

def main():
      contact_book = ContactBook()

      while True:
            print("\noptions:")
            print("1. Add Contact")
            print("2. View Contact")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter adddress: ")
                contact = Contact(name, phone, email, address)
                contact_book.add_contact(contact)
            elif choice == "2":
                contact_book.view_contact()
            elif choice == "3":
                search_term = input("Enter name or phone number to search: ")
                found_contacts = contact_book.search_contact(search_term)
                if found_contacts:
                    print("Found Contacts:")
                    for contact in found_contacts:
                        print(f"Name: {contact.name}, Phone:{contact.phone_number}, Email:{contact.email}, Address:{contact.address}")
                else:
                    print("No contacts found.")
            elif choice == "4":
                name = input("Enter name of the contact to update: ")
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                new_contact = Contact(new_name, new_phone, new_email, new_address)
                contact_book.update_contact(name, new_contact)
                print("Contact updated successfully.")
            elif choice == "5":
                name = input("Enter name of the contact to delete: ")
                contact_book.deleted_contact(name)
                print("Contact deleted successfully.")
            elif choice == "6":
                print("Thank you for using this software")
                break
            else:
                print("Invalid choice. Please select a valid option.")
   
if __name__ == "__main__":
   main()
