import pyperclip

class Contact:
    '''
	Class creates new instance of contact class
	'''
    
    contact_list = [] # Saving our contacts here by appending after executing save_contact()

    def __init__(self, first_name, last_name, phone_number, email): # This is where we're creating new instances of Contact class
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        '''
        save_contact method saves contact objects into contact_list
        '''
        Contact.contact_list.append(self) # Appending / adding new contact by appending to out contact_list[]

    def delete_contact(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''
        Contact.contact_list.remove(self) # Using the remove() method to delete the contact object from the contact_list.

    @classmethod # Simply informs the python interpreter that this is a method that belongs to the entire class
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for contact in cls.contact_list: # Loops through contact_list[]
            if contact.phone_number == number: # From return contacts, check if phone_number matches number which is passed as an argument
                return contact # returns contact with the same phone_number passed as an argument

    @classmethod
    def contact_exists(cls, number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True # return True if there's a contact with same number

        return False # returns False if no contact has the same number

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        '''
        method that copies returned contact's email to clipboard
        '''
        found_contact = Contact.find_by_number(number)
        pyperclip.copy(found_contact.email) #pyperclip.copy() method allows us to copy passed in items to the machines clipboard


