
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
        if isinstance(id, int) and id > 0:
            self._id = id
        else:
            raise ValueError("ID should be a positive integer")
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, firstname):
        if len(firstname) > 0:
            self._firstname = firstname
        else:
            raise ValueError("First Name should not be empty")

    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, lastname):
        if len(lastname) > 0:
            self._lastname = lastname
        else:
            raise ValueError("Last Name should not be empty")
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if len(email) > 0:
            self._email = email
        else:
            raise ValueError("Email should not be empty")

    @property
    def phoneNumber(self):
        return self._phoneNumber
    
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber):
        if len(phoneNumber) == 10:
            self._phoneNumber = phoneNumber
        else:
            raise ValueError("Phone Number should be 10 digits")

    def __str__(self) -> str:
        return f"Customer [id={self.id}, firstname={self.firstname}, lastname={self.lastname}, email={self.email}, phoneNumber={self.phoneNumber}]"
    
c1 = Customer()
