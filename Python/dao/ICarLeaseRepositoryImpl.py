from .ICarLeaseRepository import ICarLeaseRepository
from util.DBConnUtil import DBConnUtil
from model import *
from myexception import *
from datetime import datetime

class ICarLeaseRepositoryImpl(ICarLeaseRepository):

    def __init__(self):
        self._db_connection = DBConnUtil().getConnection()
        self._cursor = self._db_connection.cursor()
    

    # Car Management


    def addCar(self, car:Vehicle) -> None:
        query = "INSERT INTO [vehicle] ([make],[model],[year],[dailyrate],[status],[passengercapacity],[enginecapacity]) VALUES (?,?,?,?,?,?,?);"
        values = (car.make, car.model, car.year, car.dailyrate, car.status, car.passengerCapacity, car.engineCapacity)
        self._cursor.execute(query, values)
        self._db_connection.commit()
        query = "SELECT IDENT_CURRENT('vehicle') AS [id]"
        self._cursor.execute(query)
        car.id = int(self._cursor.fetchone()[0])

    def updateCarStatus(self, carID:int, status:str) -> None:
        query = "UPDATE [vehicle] SET [status] = ? WHERE [vehicleId] = ?"
        values = (status, carID)
        self._cursor.execute(query, values)
        self._db_connection.commit()
        

    def removeCar(self, carID:int):
        query1 = "SELECT * FROM [vehicle] WHERE [vehicleId] = ?"
        query2 = "DELETE FROM [vehicle] WHERE [vehicleId] = ?"
        values = (carID,)
        self._cursor.execute(query1, values)
        if self._cursor.fetchone() is None:
            raise CarNotFoundException(f"Car with ID {carID} not found")
        self._cursor.execute(query2, values)
        self._db_connection.commit()

    def listAvailableCars(self) -> list:
        query = "SELECT * FROM [vehicle] WHERE [status] = 'available'"
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        header = tuple([column[0] for column in self._cursor.description])
        result = [ header ] + result 
        return result
    
    def listRentedCars(self) -> list:
        query = "SELECT * FROM [vehicle] WHERE [status] = 'unavailable'"
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        header = tuple([column[0] for column in self._cursor.description])
        result = [ header ] + result
        return result
    
    def findCarByID(self, carID:int) -> list:
        query = "SELECT * FROM [vehicle] WHERE [vehicleId] = ?"
        self._cursor.execute(query, (carID,))
        result = self._cursor.fetchall()
        if len(result) == 0:
            raise CarNotFoundException(f"Car with ID {carID} not found")
        header = tuple([column[0] for column in self._cursor.description])
        result = [ header ] + result
        return result
    
    # Customer Management
        

    def addCustomer(self, customer:Customer) -> None:
        query = "INSERT INTO [customer] ([firstname],[lastname],[email],[phoneNumber]) VALUES (?,?,?,?)"
        values = (customer.firstname, customer.lastname, customer.email, customer.phoneNumber)
        self._cursor.execute(query, values)
        query = "SELECT IDENT_CURRENT('customer') AS [id]"
        self._cursor.execute(query)
        customer.id = int(self._cursor.fetchone()[0])
        self._db_connection.commit()
        
    def removeCustomer(self, customerID:int):
        if len(self.findCustomerByID(customerID)) == 1:
            raise CustomerNotFoundException(customerID)
        else:
            query = "DELETE FROM [customer] WHERE [customerId] = ?"
            values = (customerID,)
            self._cursor.execute(query, values)
            self._db_connection.commit()
        
    def listCustomers(self) -> list:
        query = "SELECT * FROM [customer]"
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        header = tuple([column[0] for column in self._cursor.description])
        result = [ header ] + result
        return result
    
    def findCustomerByID(self, customerID:int) -> list:
        query = "SELECT * FROM [customer] WHERE [customerId] = ?"
        self._cursor.execute(query, (customerID,))
        result = self._cursor.fetchall()
        if len(result) == 0:
            raise CustomerNotFoundException(f"Customer with ID {customerID} not found")
        header = tuple([column[0] for column in self._cursor.description])
        result = [ header ] + result
        return result
        
    # Lease Management
    
    def createLease(self, lease:Lease) -> None:
        vehicleData = self.findCarByID(lease.vehicleId)
        customerData = self.findCustomerByID(lease.customerId)

        if vehicleData[1][5] != 'Available':
            raise CarNotAvailableException(lease.vehicleId)        
        else:
            query = "INSERT INTO [lease] ([customerID],[vehicleID],[startDate],[endDate],[type]) VALUES (?,?,?,?,?)"
            values = (lease.customerId, lease.vehicleId, lease.startDate, lease.endDate, lease.type)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            query = "SELECT IDENT_CURRENT('lease') AS [id]"
            self._cursor.execute(query)
            lease.id = int(self._cursor.fetchone()[0])
            self.updateCarStatus(lease.vehicleId, 'Unavailable')
    
    def returnCar(self, leaseID:int) -> None:
        leaseData = self.findLeaseByID(leaseID)
        if len(leaseData) == 1:
            raise LeaseNotFoundException(f"Lease with ID {leaseID} not found")
        elif leaseData[1][4] is not None:
            raise Exception(f"Lease with ID {leaseID} is already returned")
        else:
            query = "UPDATE [lease] SET [endDate] = ? WHERE [leaseID] = ?"
            values = ( str(datetime.now().date()), leaseID)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self.updateCarStatus(leaseData[1][1], 'Available')

    def listActiveLeases(self) -> list:
        query = "SELECT * FROM [lease] WHERE [endDate] IS NULL"
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        header = tuple([column[0] for column in self._cursor.description])
        result = [ header ] + result
        return result
    
    def listLeaseHistory(self) -> list:
        query = "SELECT * FROM [lease]"
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        header = tuple([column[0] for column in self._cursor.description])
        result = [ header ] + result
        return result
    
    def findLeaseByID(self, leaseID:int) -> list:
        query = "SELECT * FROM [lease] WHERE [leaseID] = ?"
        self._cursor.execute(query, (leaseID,))
        result = self._cursor.fetchall()
        if len(result) == 0:
            raise LeaseNotFoundException(leaseID)
        header = tuple([column[0] for column in self._cursor.description])
        result = [ header ] + result
        return result

    # Payment Management

    def recordPayment(self, payment:Payment) -> None:
        
        leaseresult = self.findLeaseByID(payment.leaseId)
        if leaseresult[1][4] is not None:
            raise ValueError("Lease is already returned")
        leaseType = leaseresult[1][5]
        vehicleId = leaseresult[1][1]
        vehicleresult = self.findCarByID(vehicleId)
        dailyRate = vehicleresult[1][4]
        startDate = datetime.strptime(leaseresult[1][3], '%Y-%m-%d')
        endDate = datetime.strptime(payment.paymentDate, '%Y-%m-%d')
        noOfDay = (endDate - startDate).days
        if noOfDay == 0:
            noOfDay = 1
        amount = dailyRate * noOfDay
        if amount < payment.amount:
            raise Exception(f"Amount paid is more than the lease amount! Your current due is {amount}")
        elif amount > payment.amount:
            raise Exception(f"Amount paid is less than the lease amount! Make sure the amount is correct. Your current due is {amount}")
        query = "INSERT INTO [payment] ([leaseID],[amount],[paymentdate]) VALUES (?,?,?)"
        values = (payment.leaseId, payment.amount, payment.paymentDate)
        self._cursor.execute(query, values)
        self._db_connection.commit()
        query = "SELECT IDENT_CURRENT('payment') AS [id]"
        self._cursor.execute(query)
        payment.id = int(self._cursor.fetchone()[0])