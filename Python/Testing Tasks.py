import unittest
from dao import ICarLeaseRepositoryImpl as LeaseManager
from model import *
from myexception.exceptions import *
from pprint import pprint 

class TestingCustomerService(unittest.TestCase):

    
    def setUp(self) -> None:
        self.lease_manager = LeaseManager()

         # Test data for test case 1
        self.car = Vehicle()
        self.car.make = 'volkswagen'
        self.car.model = 'Polo'
        self.car.year = '2023'
        self.car.dailyrate = 2000.5
        self.car.status = 'Available'
        self.car.passengerCapacity = 7
        self.car.engineCapacity = 1000

        # Test data for test case 2

        self.lease = Lease()
        self.lease.customerId = 11
        self.lease.vehicleId = 2
        self.lease.startDate = '2024-05-01'
        self.lease.type = 'Daily'

        # Test data for test case 3
        self.validCustomer = Customer()
        self.validCustomer.firstname = 'John'
        self.validCustomer.lastname = 'Doe'
        self.validCustomer.email = 'john.de0@randommail.com'
        self.validCustomer.phoneNumber = '1234567898'

        # Test data for test case 4
        self.validLeaseID = 3
        self.findLeaseByIDResult = [(3,3,3,'2024-05-03','2024-05-04','Daily')]

        # Test data for test case 5
        self.InvalidCustomerID = 1000
        self.InvalidCarID = 1000
        self.invalidLeaseID = 1000


        
# Testing 'Add Car' function
    def test_add_car(self):
        print("Testing 'Add Car' function")
        self.lease_manager.addCar(self.car)
        producedResult = self.lease_manager.findCarByID(self.car.id)
        expectedResult = [ (self.car.id, 'volkswagen', 'Polo', '2023', 2000.5, 'Available', 7, 1000) ]
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[1][i], expectedResult[0][i])

#Testing lease is created successfully or not
    def test_create_lease(self):
        print("Testing 'Create Lease' function")
        self.lease_manager.createLease(self.lease)
        producedResult = self.lease_manager.findLeaseByID(self.lease.id)
        expectedResult = [ (self.lease.id, self.lease.vehicleId, self.lease.customerId, self.lease.startDate, self.lease.endDate, self.lease.type) ]
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[1][i], expectedResult[0][i]) #Starting from 1 because the first row is the header

#Testing lease is retrieved by ID or not
    def test_find_lease_by_id(self):
        print("Testing 'Lease By ID' function")
        producedResult = self.lease_manager.findLeaseByID(self.validLeaseID)
        expectedResult = self.findLeaseByIDResult
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[1][i], expectedResult[0][i]) #Starting from 1 because the first row is the header

#Testing if exception is raised when car ID, customer ID, lease ID not found
    def test_customer_display_fail(self):
            print("Testing 'Customer By ID' function with invalid ID")
            with self.assertRaises(CustomerNotFoundException):
                self.lease_manager.findCustomerByID(self.InvalidCustomerID)

    def test_car_display_fail(self):
            print("Testing 'Car By ID' function with invalid ID")
            with self.assertRaises(CarNotFoundException):
                self.lease_manager.findCarByID(self.InvalidCarID)

    def test_find_lease_by_id_fail(self):
            print("Testing 'Lease By ID' function with invalid ID")
            with self.assertRaises(LeaseNotFoundException):
                self.lease_manager.findLeaseByID(self.invalidLeaseID)

if __name__ == "__main__":
    unittest.main()
    print("Testing complete.")