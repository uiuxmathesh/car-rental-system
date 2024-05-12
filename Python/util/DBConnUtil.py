from .PropertyUtil import PropertyUtil
import pyodbc

class DBConnUtil:

    connection = None

    @staticmethod
    def getConnection():
        if DBConnUtil.connection is None:
            connectionString = PropertyUtil.getPropertytring()
            DBConnUtil.connection = pyodbc.connect(connectionString)
        return DBConnUtil.connection
    
    @staticmethod
    def closeConnection():
        if DBConnUtil.connection is not None:
            DBConnUtil.connection.close()
            DBConnUtil.connection = None