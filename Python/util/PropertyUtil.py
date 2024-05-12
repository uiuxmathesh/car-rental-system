

class PropertyUtil:

    @staticmethod
    def getPropertytring():
        server_name = "Mathesh-PC"
        database_name = "testing"
        trusted_connection = "Yes"
        connectionString = f"Driver={{SQL Server}}; Server={server_name}; Database={database_name}; Trusted_Connection={trusted_connection}"
        return connectionString