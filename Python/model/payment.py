from datetime import datetime
class Payment:

    def __init__(self) -> None:
        self._id = None
        self._leaseId = None
        self._amount = None
        self._paymentDate = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int) and id > 0:
            self._id = id
        else:
            raise ValueError("ID should be a positive integer")
    
    @property
    def leaseId(self):
        return self._leaseId
    
    @leaseId.setter
    def leaseId(self, leaseId):
        if isinstance(leaseId, int) and leaseId > 0:
            self._leaseId = leaseId
        else:
            raise ValueError("Lease ID should be a positive integer")   

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if isinstance(amount, float) and amount > 0:
            self._amount = amount
        else:
            raise ValueError("Please enter a valid amount")
        self._amount = amount

    @property
    def paymentDate(self):
        return self._paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        paymentDate = str(datetime.strptime(paymentDate, "%Y-%m-%d").date())
        self._paymentDate = paymentDate

    def __str__(self) -> str:
        return f"Payment ID: {self.id}, Lease ID: {self.leaseId}, Amount: {self.amount}, Payment Date: {self.paymentDate}"
    