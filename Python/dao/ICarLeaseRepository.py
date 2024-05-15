from abc import ABC, abstractmethod

class ICarLeaseRepository(ABC):
    
    # Car Management
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

    # Customer Management
            
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

    # Lease Management
        
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

    # Payment Management
    @abstractmethod
    def recordPayment(self, payment) -> None:
        pass
