
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
        if isinstance(id, int) and id > 0:
            self._id = id
        else:
            raise ValueError("ID should be a positive integer")

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        if len(make) > 0:
            self._make = make
        else:
            raise ValueError("Make should not be empty")

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self,model):
        if len(model) > 0:
            self._model = model
        else:
            raise ValueError("Model should not be empty")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self,year):
        if len(year) == 4:
            self._year = year
        else:
            raise ValueError("Year should be in YYYY format") 

    @property
    def dailyrate(self):
        return self._dailyrate
    
    @dailyrate.setter
    def dailyrate(self,dailyrate):
        if dailyrate > 0:
            self._dailyrate = dailyrate
        else:
            raise ValueError("Daily rate should be a positive number")
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,status):
        if not isinstance(status,str):
            raise ValueError("Status should be a string")
        if status.capitalize() in ['Available','Unavailable']:
            self._status = status
        else:
            raise ValueError("Status should be either Available or Unavailable")

    @property
    def passengerCapacity(self):
        return self._passengerCapacity
    
    @passengerCapacity.setter
    def passengerCapacity(self,passesngerCapacity):
        if passesngerCapacity > 4:
            self._passengerCapacity = passesngerCapacity
        else:
            raise ValueError("Passenger capacity should be greater than 4")
    
    @property
    def engineCapacity(self):
        return self._engineCapacity
    
    @engineCapacity.setter
    def engineCapacity(self,engineCapacity):
        if engineCapacity > 0:
            self._engineCapacity = engineCapacity
        else:
            raise ValueError("Engine capacity should be a positive number")
        

    def __str__(self) -> str:
        return f"Vehicle [id={self.id}, make={self.make}, model={self.model}, year={self.year}, dailyrate={self.dailyrate}, status={self.status}, passengerCapacity={self.passengerCapacity}, engineCapacity={self.engineCapacity}]"


