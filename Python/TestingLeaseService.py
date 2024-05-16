import unittest
from dao import ICarLeaseRepositoryImpl as LeaseManager
from model import *
from myexception.exceptions import *
from pprint import pprint 
from datetime import datetime

class TestingLeaseService(unittest.TestCase):

    def setUp(self) -> None:
        self.lease_manager = LeaseManager()

        # Test data for test case 1
        self.lease = Lease()
        self.lease.customerId = 11
        self.lease.vehicleId = 8
        self.lease.startDate = '2024-05-01'
        self.lease.type = 'Daily'

        # Test data for test case 2
        self.invalidlease = Lease()
        self.invalidlease.customerId = 9
        self.invalidlease.vehicleId = 8
        self.invalidlease.startDate = '2024-05-01'
        self.invalidlease.type = 'Daily'


        # Test data for test case 2
        self.validLeaseID = 3
        self.findLeaseByIDResult = [(3,3,3,'2024-05-03','2024-05-04','Daily')]

        # Test data for test case 3
        self.invalidLeaseID = 1000

        # Test data for test case 6
        self.validActiveLeaseID = 4

        # Test data for test case 7
        self.inactiveLeaseID = 5

    # Test case 1: Creating a lease with valid data
    def test_create_lease(self):
        print("Testing 'Create Lease' function")
        self.lease_manager.createLease(self.lease)
        producedResult = self.lease_manager.findLeaseByID(self.lease.id)
        expectedResult = [ (self.lease.id, self.lease.vehicleId, self.lease.customerId, self.lease.startDate, self.lease.endDate, self.lease.type) ]
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[1][i], expectedResult[0][i]) #Starting from 1 because the first row is the header

    # Test case 2: Creating a lease with invalid data
    def test_create_lease_fail(self):
        print("Testing 'Create Lease' function with invalid data")
        with self.assertRaises(CarNotAvailableException):
            self.lease_manager.createLease(self.invalidlease)



    # Test case 3: Finding a lease by Valid ID
    def test_find_lease_by_id(self):
        print("Testing 'Lease By ID' function")
        producedResult = self.lease_manager.findLeaseByID(self.validLeaseID)
        expectedResult = self.findLeaseByIDResult
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[1][i], expectedResult[0][i]) #Starting from 1 because the first row is the header

    # Test case 4: Finding a lease by Invalid ID
    def test_find_lease_by_id_fail(self):
        print("Testing 'Lease By ID' function with invalid ID")
        with self.assertRaises(LeaseNotFoundException):
            self.lease_manager.findLeaseByID(self.invalidLeaseID)

    # Test case 5: Listing all active leases
    def test_list_active_leases(self):
        print("Testing 'List Active Leases' function")
        producedResult = self.lease_manager.listActiveLeases()
        for result in producedResult[1:]:
            self.assertTrue(result[4] == None)

    # Test case 6: Listing all lease history
    def test_list_lease_history(self):
        print("Testing 'List Lease History' function")
        producedResult = self.lease_manager.listLeaseHistory()
        self.assertTrue(len(producedResult) > 0)
        for result in producedResult[1:]:
            self.assertTrue(len(result) > 0)

    # Test case 7: Returning a car for active lease
    def test_return_car(self):
        print("Testing 'Return Car' function")
        self.lease_manager.returnCar(self.validActiveLeaseID)
        producedResult = self.lease_manager.findLeaseByID(self.validActiveLeaseID) 
        self.assertTrue(producedResult[1][4] == str(datetime.now().date()))

    # Test case 8: Returning a car for inactive lease
    def test_return_car_fail(self):
        print("Testing 'Return Car' function with inactive lease")
        with self.assertRaises(Exception):
            self.lease_manager.returnCar(self.inactiveLeaseID)



if __name__ == "__main__":
    unittest.main()
    print("Testing complete.")


       