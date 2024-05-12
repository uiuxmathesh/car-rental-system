from ICarLeaseRepository import ICarLeaseRepository
from util.DBConnUtil import DBConnUtil
from model import *
from myexception import *

class ICarLeaseRepositoryImpl(ICarLeaseRepository):

    class CarManagement:

        def __init__(self):
            self._db_connection = DBConnUtil().getConnection()
            self._cursor = self._db_connection.cursor()

        def addCar(self, car:Vehicle) -> None:
            query = "INSERT INTO [vehicle] ([make],[model],[year],[dailyrate],[status],[passengercapacity],[enginecapacity]) VALUES (?,?,?,?,?,?,?)"
            values = (car.make, car.model, car.year, car.dailyrate, car.status, car.passengerCapacity, car.engineCapacity)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

        def removeCar(self, carID:int):
            query = "DELETE FROM [vehicle] WHERE [id] = ?"
            values = (carID,)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()


        def listAvailableCars(self) -> list:
            query = "SELECT * FROM [vehicle] WHERE [status] = 'available'"
            self._cursor.execute(query)
            return self._cursor.fetchall()

        def listRentedCars(self) -> list:
            query = "SELECT * FROM [vehicle] WHERE [status] = 'unavailable'"
            self._cursor.execute(query)
            return self._cursor.fetchall()

        def findCarByID(self, carID:int) -> list:
            query = "SELECT * FROM [vehicle] WHERE [id] = ?"
            self._cursor.execute(query, (carID,))
            return self._cursor.fetchall()

    class CustomerManagement:
        
        def __init__(self):
            self._db_connection = DBConnUtil().getConnection()
            self._cursor = self._db_connection.cursor()

        def addCustomer(self, customer:Customer) -> None:
            query = "INSERT INTO [customer] ([firstname],[lastname],[email],[phone]) VALUES (?,?,?,?)"
            values = (customer.firstname, customer.lastname, customer.email, customer.phone)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

        def removeCustomer(self, customerID:int):
            query = "DELETE FROM [customer] WHERE [id] = ?"
            values = (customerID,)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

        def listCustomers(self) -> list:
            query = "SELECT * FROM [customer]"
            self._cursor.execute(query)
            return self._cursor.fetchall()

        def findCustomerByID(self, customerID:int) -> list:
            query = "SELECT * FROM [customer] WHERE [id] = ?"
            self._cursor.execute(query, (customerID,))
            return self._cursor.fetchall()
        
    class LeaseManagement:

        def __init__(self):
            self._db_connection = DBConnUtil().getConnection()
            self._cursor = self._db_connection.cursor()
        
        def createLease(self, lease:Lease) -> None:
            query = "INSERT INTO [lease] ([customerID],[vehicleID],[startDate],[endDate],[type]) VALUES (?,?,?,?,?)"
            values = (lease.customerId, lease.vehicleId, lease.startDate, lease.endDate, lease.type)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

        def returnCar(self, leaseID:int) -> None:
            query = "DELETE FROM [lease] WHERE [id] = ?"
            values = (leaseID,)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()

    class PaymentManagement:

        def recordPayment(self, payment:Payment) -> None:
            query = "INSERT INTO [payment] ([leaseID],[amount],[date]) VALUES (?,?,?)"
            values = (payment.leaseId, payment.amount, payment.paymentDate)
            self._cursor.execute(query, values)
            self._db_connection.commit()
            self._cursor.close()
            self._db_connection = DBConnUtil().closeConnection()
