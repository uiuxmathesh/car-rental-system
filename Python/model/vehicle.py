
class Vehicle:

    def __init__(self) -> None:
        self._id = None
        self._make = None
        self._model = None
        self._year = None
        self._dailyrate = None
        self._status = None
        self._passengerCapacity = None
        self._engineCapacity = None

    @property
    def id(self):
        return self._id

    @id.setter
    def  id(self,id):
        self._id = id

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self,model):
        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self,year):
        self._year = year 

    @property
    def dailyrate(self):
        return self._dailyrate
    
    @dailyrate.setter
    def dailyrate(self,dailyrate):
        self._dailyrate = dailyrate
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,status):
        self._status = status

    @property
    def passengerCapacity(self):
        return self._passengerCapacity
    
    @passengerCapacity.setter
    def passengerCapacity(self,passesngerCapacity):
        self._passengerCapacity = passesngerCapacity
    
    @property
    def engineCapacity(self):
        return self._engineCapacity
    
    @engineCapacity.setter
    def engineCapacity(self,engineCapacity):
        self._engineCapacity= engineCapacity

    def __str__(self) -> str:
        return f"Vehicle [id={self.id}, make={self.make}, model={self.model}, year={self.year}, dailyrate={self.dailyrate}, status={self.status}, passengerCapacity={self.passengerCapacity}, engineCapacity={self.engineCapacity}]"

# v1 = Vehicle()
# v1.id = 1
# print(v1.id)
# v1.make ='Honda'
# print(v1.make)
# v1.model = 'Amaze'
# print(v1.model)
# v1.dailyrate = 200
# print(v1.dailyrate)
# v1.status = 'Available'
# print(v1.status)
# v1.engineCapacity = 400
# print(v1.engineCapacity)
# v1.passengerCapacity = 5
# print(v1.passengerCapacity)
