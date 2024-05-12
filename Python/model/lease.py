
class Lease:

    def __init__(self) -> None:
        self._id = None
        self._vehicleId = None
        self._customerId = None
        self._startDate = None
        self._endDate = None
        self._type = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def vehicleId(self):
        return self._vehicleId
    
    @vehicleId.setter
    def vehicleId(self, vehicleId):
        self._vehicleId = vehicleId

    @property
    def customerId(self):
        return self._customerId
    
    @customerId.setter
    def customerId(self, customerId):
        self._customerId = customerId

    @property
    def startDate(self):
        return self._startDate
    
    @startDate.setter
    def startDate(self, startDate):
        self._startDate = startDate

    @property
    def endDate(self):
        return self._endDate
    
    @endDate.setter
    def endDate(self, endDate):
        self._endDate = endDate

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type

    