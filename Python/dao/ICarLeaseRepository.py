from abc import ABC, abstractmethod

class ICarLeaseRepository(ABC):
    
    # Car Management
    @abstractmethod
    def addCar(self, car) -> None:
        """Adds a new Car to the Database"""
        pass

    @abstractmethod
    def removeCar(self, carID):
        """Removes a Car from the Database"""
        pass

    @abstractmethod
    def listAvailableCars(self) -> list:
        """Lists all cars where status='Available'"""
        pass

    @abstractmethod
    def listRentedCars(self) -> list:
        """Lists all cars where status='Unavailable'"""
        pass

    @abstractmethod
    def findCarByID(self, carID) -> list:
        """Finds a Car by ID"""
        pass

    # Customer Management
            
    @abstractmethod
    def addCustomer(self, customer) -> None:
        """Adds a new Customer to the Database"""
        pass

    @abstractmethod
    def removeCustomer(self, customerID):
        """Removes a Customer from the Database"""
        pass

    @abstractmethod
    def listCustomers(self) -> list:
        """Lists all Customers"""
        pass

    @abstractmethod
    def findCustomerByID(self, customerID) -> list:
        """Finds a Customer by ID"""
        pass

    # Lease Management
        
    @abstractmethod
    def createLease(self, lease) -> None:
        """Creates a new Lease for a Customer and a Car"""
        pass

    @abstractmethod
    def returnCar(self, leaseID) -> None:
        """Ends a Lease and returns the Car"""
        pass

    @abstractmethod
    def listActiveLeases(self) -> list:
        """Lists all active Leases"""
        pass
    
    @abstractmethod
    def listLeaseHistory(self) -> list:
        """Lists all Leases"""
        pass

    # Payment Management
    @abstractmethod
    def recordPayment(self, payment) -> None:
        """Records a Payment"""
        pass
