

class Employee:
    def __init__(self , name , _salary , __ssn):
        self.name = name
        self._salary = _salary      
        self.__ssn = __ssn 

c1 = Employee("ali", 234550 , "123-45-6789")

print("public:", c1.name)

print("protected:", c1._salary)

try:
    print("private:" , c1.__ssn)
except AttributeError as e:
    print("Private: Cannot access directly -->", e)

print("Private via name mangling:", c1._Employee__ssn)
