from .ICarLeaseRepository import ICarLeaseRepository
from util.DBConnUtil import DBConnUtil
from model import *
from myexception import *

class ICarLeaseRepositoryImpl(ICarLeaseRepository):

    def __init__(self):
        self._db_connection = DBConnUtil().getConnection()
        self._cursor = self._db_connection.cursor()
    

    class CarManagement:

        def __init__(self):
            self._db_connection = DBConnUtil().getConnection()
            self._cursor = self._db_connection.cursor()

        def addCar(self, car:Vehicle) -> None:
            query = "INSERT INTO [vehicle] ([make],[model],[year],[dailyrate],[status],[passengercapacity],[enginecapacity]) VALUES (?,?,?,?,?,?,?);"
            values = (car.make, car.model, car.year, car.dailyrate, car.status, car.passengerCapacity, car.engineCapacity)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            query = "SELECT IDENT_CURRENT('vehicle') AS [id]"
            self._cursor.execute(query)
            car.id = int(self._cursor.fetchone()[0])
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

        def removeCar(self, carID:int):
            query1 = "SELECT * FROM [vehicle] WHERE [id] = ?"
            query2 = "DELETE FROM [vehicle] WHERE [id] = ?"
            values = (carID,)
            self._cursor.execute(query1, values)
            if self._cursor.fetchone() is None:
                raise CarNotFoundException(f"Car with ID {carID} not found")
            self._cursor.execute(query2, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()


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
            header = tuple([column[0] for column in self._cursor.description])
            result = [ header ] + result
            return result

    class CustomerManagement:
        
        def __init__(self):
            self._db_connection = DBConnUtil().getConnection()
            self._cursor = self._db_connection.cursor()

        def addCustomer(self, customer:Customer) -> None:
            query = "INSERT INTO [customer] ([firstname],[lastname],[email],[phoneNumber]) VALUES (?,?,?,?)"
            values = (customer.firstname, customer.lastname, customer.email, customer.phone)
            self._cursor.execute(query, values)
            query = "SELECT IDENT_CURRENT('customer') AS [id]"
            self._cursor.execute(query)
            customer.id = int(self._cursor.fetchone()[0])
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

        def removeCustomer(self, customerID:int):
            query = "DELETE FROM [customer] WHERE [customerId] = ?"
            values = (customerID,)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

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
            header = tuple([column[0] for column in self._cursor.description])
            result = [ header ] + result
            return result
        
    class LeaseManagement:

        def __init__(self):
            self._db_connection = DBConnUtil().getConnection()
            self._cursor = self._db_connection.cursor()
        
        def createLease(self, lease:Lease) -> None:
            query = "INSERT INTO [lease] ([customerID],[vehicleID],[startDate],[endDate],[type]) VALUES (?,?,?,?,?)"
            values = (lease.customerId, lease.vehicleId, lease.startDate, lease.endDate, lease.type)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            query = "SELECT IDENT_CURRENT('lease') AS [id]"
            self._cursor.execute(query)
            lease.id = int(self._cursor.fetchone()[0])
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

        def returnCar(self, leaseID:int) -> None:
            query = "UPDATE [lease] SET [endDate] = ? WHERE [leaseID] = ?"
            values = (leaseID,)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

        def listActiveLeases(self) -> list:
            query = "SELECT * FROM [lease] WHERE [endDate] IS NULL"
            self._cursor.execute(query)
            result = self._cursor.fetchall()
            header = tuple([column[0] for column in self._cursor.description])
            result = [ header ] + result
            return result
        
        def listLeaseHistory(self) -> list:
            query = "SELECT * FROM [lease] WHERE [endDate] IS NOT NULL"
            self._cursor.execute(query)
            result = self._cursor.fetchall()
            header = tuple([column[0] for column in self._cursor.description])
            result = [ header ] + result
            return result
        
        def findLeaseByID(self, leaseID:int) -> list:
            query = "SELECT * FROM [lease] WHERE [leaseID] = ?"
            self._cursor.execute(query, (leaseID,))
            result = self._cursor.fetchall()
            header = tuple([column[0] for column in self._cursor.description])
            result = [ header ] + result
            return result

    class PaymentManagement:

        def recordPayment(self, payment:Payment) -> None:
            query = "INSERT INTO [payment] ([leaseID],[amount],[date]) VALUES (?,?,?)"
            values = (payment.leaseId, payment.amount, payment.paymentDate)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            query = "SELECT IDENT_CURRENT('payment') AS [id]"
            self._cursor.execute(query)
            payment.id = int(self._cursor.fetchone()[0])
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()
