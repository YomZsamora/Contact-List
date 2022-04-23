from re import S
import unittest
from contact import Contact
import pyperclip

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("Yommie", "Samora", "0711432765", "samaurah@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.first_name, "Yommie") 
        self.assertEqual(self.new_contact.last_name, "Samora")
        self.assertEqual(self.new_contact.phone_number, "0711432765")
        self.assertEqual(self.new_contact.email, "samaurah@gmail.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Contact.contact_list = [] # Empty the contact_list


    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list), 1) # Checks if we have the contact saved in our contact_list[]

    def test_save_multiple_contact(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_contact.save_contact() # saving the new contact
        test_contact = Contact("Test", "User", "0712345678","test@user.com") # another new contact_list
        test_contact.save_contact() # saving the second new contact
        self.assertEqual(len(Contact.contact_list), 2) # Checks if we have the two contacts in our contact_list[]

    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        test_contact = Contact("Test", "User", "0712345678","test@user.com") # another new contact_list
        test_contact.save_contact() # saving the second new contact

        self.new_contact.delete_contact() # Deleting a contact object
        self.assertEqual(len(Contact.contact_list), 1) # Two contacts were saved then one deleted. SHould have one contact left

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''
        self.new_contact.save_contact() # saving the new contact
        test_contact = Contact("Test", "User", "0712345678","test@user.com") # another new contact_list
        test_contact.save_contact() # saving the second new contact

        found_contact = Contact.find_by_number("0712345678") # Pass phone_number to find_by_number() to return existing contact with the same number
        self.assertEqual(found_contact.email, test_contact.email) # Checks if emails are same from created contact and return contact with same number

    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''
        self.new_contact.save_contact() # saving the new contact
        test_contact = Contact("Test", "User", "0712345678","test@user.com") # another new contact_list
        test_contact.save_contact() # saving the second new contact

        contact_exists = Contact.contact_exists("0712345678") # Pass phone_number to contact_exists() to return existing contact with the same number
        self.assertTrue(contact_exists) 

    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''
        self.assertEqual(Contact.display_contacts(), Contact.contact_list) # display_contacts() should return the same contacts in our contact_list


    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''
        self.new_contact.save_contact() # saving the new contact
        Contact.copy_email("0711432765") # First confirm that the contact exists
        self.assertEqual(self.new_contact.email, pyperclip.paste()) # In our assertEqual method we use pyperclip.paste(), and compare it with the contact object email.


if __name__ == "__main__":
    unittest.main()