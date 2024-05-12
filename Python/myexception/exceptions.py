
class CarNotFoundException(Exception):
    def __init__(self, id:int):
        message = f"Car with ID {id} not found"
        super().__init__(message)

class CustomerNotFoundException(Exception):
    def __init__(self, id:int):
        message = f"Customer with ID {id} not found"
        super().__init__(message)

class LeaseNotFoundException(Exception):
    def __init__(self, id:int):
        message = f"Lease with ID {id} not found"
        super().__init__(message)

