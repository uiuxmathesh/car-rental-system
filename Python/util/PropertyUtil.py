from json import dump
from json import load

class PropertyUtil:

    @staticmethod
    def getPropertytring():
        with open(r"util\\config.json",'r') as file:
            property = load(file)
        
        # print(type(property))
        SERVER_NAME = property.get("server")
        DATABASE_NAME = property.get("database")
        TRUSTED_CONNECTION = property.get("trusted_connection")
        CONNECTION_STRING = f"Driver={{SQL Server}}; Server={SERVER_NAME}; Database={DATABASE_NAME}; Trusted_Connection={TRUSTED_CONNECTION}"
        return CONNECTION_STRING
    

# print(PropertyUtil.getPropertytring())