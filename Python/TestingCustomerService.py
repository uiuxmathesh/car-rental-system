import unittest
from dao import ICarLeaseRepositoryImpl as LeaseManager
from model import *
from myexception.exceptions import *
from pprint import pprint 

class TestingCustomerService(unittest.TestCase):

    # Testing all the customer management functions
    def setUp(self) -> None:
        self.lease_manager = LeaseManager()
        # Test data for test case 1
        self.customerID = 5
        self.findCustomerByIDResult = [(5, 'David', 'Lee', 'david.lee@example.com', '234-567-8901')]

        # Test data for test case 2
        self.InvalidCustomerID = 1000

        # Test data for test case 3
        self.validCustomer = Customer()
        self.validCustomer.firstname = 'John'
        self.validCustomer.lastname = 'Doe'
        self.validCustomer.email = 'john.de0@randommail.com'
        self.validCustomer.phoneNumber = '1234567898'


    #Test Case 1: Testing 'Customer By ID' function with Valid ID
    def test_customer_display(self):
        print("Testing 'Customer By ID' function")
        producedResult = self.lease_manager.findCustomerByID(self.customerID)
        expectedResult = self.findCustomerByIDResult
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[1][i], expectedResult[0][i]) #Starting from 1 because the first row is the header

    #Test Case 2: Testing 'Customer By ID' function with Invalid ID
    def test_customer_display_fail(self):
        print("Testing 'Customer By ID' function with invalid ID")
        with self.assertRaises(CustomerNotFoundException):
            self.lease_manager.findCustomerByID(self.InvalidCustomerID)

    #Test Case 3: Testing 'Add Customer' function with Valid Data
    def test_add_customer(self):
        print("Testing 'Add Customer' function")
        
        self.lease_manager.addCustomer(self.validCustomer)
        producedResult = self.lease_manager.findCustomerByID(self.validCustomer.id)
        expectedResult = [ (self.validCustomer.id, self.validCustomer.firstname, self.validCustomer.lastname, self.validCustomer.email, self.validCustomer.phoneNumber) ]
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[1][i], expectedResult[0][i]) #Starting from 1 because the first row is the header

    #Test Case 4: Testing 'List Customers' function
    def test_list_customers(self):
        print("Testing 'List Customers' function")
        producedResult = self.lease_manager.listCustomers()
        self.assertTrue(len(producedResult) > 0)
        for result in producedResult[1:]:
            self.assertTrue(len(result) > 0)
            
    #Test Case 5: Testing 'Remove Customer' function
    def test_remove_customer(self):
        print("Testing 'Remove Customer' function")
        self.lease_manager.removeCustomer(self.validCustomer.id)
        with self.assertRaises(CustomerNotFoundException):
            self.lease_manager.findCustomerByID(self.validCustomer.id)
        


if __name__ == "__main__":
    unittest.main()
    print("Testing complete.")
