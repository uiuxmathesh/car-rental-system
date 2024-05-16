from datetime import datetime
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
        if isinstance(id, int) and id > 0:
            self._id = id
        else:
            raise ValueError("ID should be a positive integer")
    
    @property
    def vehicleId(self):
        return self._vehicleId
    
    @vehicleId.setter
    def vehicleId(self, vehicleId):
        if isinstance(vehicleId, int) and vehicleId > 0:
            self._vehicleId = vehicleId 
        else:
            raise ValueError("Vehicle ID should be a positive integer")

    @property
    def customerId(self):
        return self._customerId
    
    @customerId.setter
    def customerId(self, customerId):
        if isinstance(customerId, int) and customerId > 0:
            self._customerId = customerId
        else:
            raise ValueError("Customer ID should be a positive integer")

    @property
    def startDate(self):
        return self._startDate
    
    @startDate.setter
    def startDate(self, startDate):
        startDate = str(datetime.strptime(startDate, "%Y-%m-%d").date())
        self._startDate = startDate

    @property
    def endDate(self):
        return self._endDate
    
    @endDate.setter
    def endDate(self, endDate):
        endDate = str(datetime.strptime(endDate, "%Y-%m-%d").date())
        self._endDate = endDate

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if type in ["Daily", "Monthly"]:  
            self._type = type
        else:
            raise ValueError("Type should be Daily or Monthly")

    def __str__(self) -> str:
        return f"Lease [id={self.id}, vehicleId={self.vehicleId}, customerId={self.customerId}, startDate={self.startDate}, endDate={self.endDate}, type={self.type}]"
    