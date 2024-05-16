class CarNotFoundException(Exception):
    def __init__(self, id: int):
        """Raised when a car is not found in the database"""
        message = f"Car with ID {id} not found"
        super().__init__(message)


class CustomerNotFoundException(Exception):
    def __init__(self, id: int):
        """Raised when a customer is not found in the database"""
        message = f"Customer with ID {id} not found"
        super().__init__(message)


class LeaseNotFoundException(Exception):
    def __init__(self, id: int):
        """Raised when a lease is not found in the database"""
        message = f"Lease with ID {id} not found"
        super().__init__(message)


## My Exception
class CarNotAvailableException(Exception):
    def __init__(self, id: int):
        """Raised when a car is not available for lease"""
        message = f"Car with ID {id} is not available"
        super().__init__(message)
