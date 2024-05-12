
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
        self._id = id
    
    @property
    def leaseId(self):
        return self._leaseId
    
    @leaseId.setter
    def leaseId(self, leaseId):
        self._leaseId = leaseId

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def paymentDate(self):
        return self._paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        self._paymentDate = paymentDate
    