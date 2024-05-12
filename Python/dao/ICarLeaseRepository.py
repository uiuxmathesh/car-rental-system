from abc import ABC, abstractmethod

class ICarLeaseRepository(ABC):

    class CarManagement:

        @abstractmethod
        def addCar(self, car) -> None:
            pass

        @abstractmethod
        def removeCar(self, carID):
            pass

        @abstractmethod
        def listAvailableCars(self) -> list:
            pass

        @abstractmethod
        def listRentedCars(self) -> list:
            pass

        @abstractmethod
        def findCarByID(self, carID) -> list:
            pass

    class CustomerManagement:
            
        @abstractmethod
        def addCustomer(self, customer) -> None:
            pass

        @abstractmethod
        def removeCustomer(self, customerID):
            pass

        @abstractmethod
        def listCustomers(self) -> list:
            pass

        @abstractmethod
        def findCustomerByID(self, customerID) -> list:
            pass

    class LeaseManagement:
        
        @abstractmethod
        def createLease(self, lease) -> None:
            pass

        @abstractmethod
        def returnCar(self, leaseID) -> None:
            pass

        @abstractmethod
        def listActiveLeases(self) -> list:
            pass

        @abstractmethod
        def listLeaseHistory(self) -> list:
            pass

    class PaymentManagement:

        @abstractmethod
        def recordPayment(self, payment) -> None:
            pass
