import unittest
from dao import ICarLeaseRepositoryImpl as LeaseManager
from model import *
from myexception.exceptions import *
from pprint import pprint 

class TestingCarService(unittest.TestCase):


    # Testing all the car management functions
    def setUp(self) -> None:
        self.lease_manager = LeaseManager()
        # Test data for test case 1
        self.carID = 5
        self.findCarByIDResult = [(5, 'Suzuki', 'Ignis', '2023', 200.5, 'Available', 5, 400)]
        self.car = Vehicle()

        # Test data for test case 2
        self.car.make = 'volkswagen'
        self.car.model = 'Polo'
        self.car.year = '2023'
        self.car.dailyrate = 2000.5
        self.car.status = 'Available'
        self.car.passengerCapacity = 7
        self.car.engineCapacity = 1000

        # Test data for test case 3
        self.deleteCarId = 42

    # def tearDown(self) -> None:
    #     self.lease_manager = None
    #     self.car = None
        

    # Testing 'Car By ID' function
    def test_car_display(self):
        print("Testing 'Car By ID' function")
        producedResult = self.lease_manager.findCarByID(self.carID)
        expectedResult = self.findCarByIDResult
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[1][i], expectedResult[0][i]) #Starting from 1 because the first row is the header
    
    def test_car_display_fail(self):
        print("Testing 'Car By ID' function with invalid ID")
        with self.assertRaises(CarNotFoundException):
            self.lease_manager.findCarByID(1000)

    # Testing 'Add Car' function
    def test_add_car(self):
        print("Testing 'Add Car' function")
        self.lease_manager.addCar(self.car)
        producedResult = self.lease_manager.findCarByID(self.car.id)
        expectedResult = [ (self.car.id, 'volkswagen', 'Polo', '2023', 2000.5, 'Available', 7, 1000) ]
        numOfColumns = len(producedResult[0])
        for i in range(numOfColumns):
            self.assertEqual(producedResult[0][i], expectedResult[0][i])

    # Testing 'List Available Cars' function
    def test_list_available_cars(self):
        print("Testing 'List Available Cars' function")
        producedResult = self.lease_manager.listAvailableCars()
        for result in producedResult[1:]:
            if result[5] != 'Available':
                self.fail("Car status is not available")

    # Testing 'List Rented Cars' function
    def test_list_rented_cars(self):
        print("Testing 'List Rented Cars' function")
        producedResult = self.lease_manager.listRentedCars()
        for result in producedResult[1:]:
            if result[5] != 'Unavailable':
                self.fail("Car status is not unavailable")
        
    # Testing 'Remove Car' function
    def test_remove_car(self):
        print("Testing 'Remove Car' function")
        self.lease_manager.removeCar(self.deleteCarId)
        with self.assertRaises(CarNotFoundException):
            self.lease_manager.findCarByID(self.deleteCarId)

    def test_remove_car_id_not_exists(self):
        print("Testing 'Remove Car' function with invalid ID")
        with self.assertRaises(CarNotFoundException):
            self.lease_manager.removeCar(1000)


    


if __name__ == "__main__":
    unittest.main()
    print("Testing complete.")