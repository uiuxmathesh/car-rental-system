
class Customer:

    def __init__(self) -> None:
        self._id = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._phoneNumber = None

    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phoneNumber(self):
        return self._phoneNumber
    
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def __str__(self) -> str:
        return f"Customer [id={self.id}, firstname={self.firstname}, lastname={self.lastname}, email={self.email}, phoneNumber={self.phoneNumber}]"
    