
# class Student:

#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks 

#     def display(self):
#         print(f"name: {self.name} marks:{self.marks}") 

# s1 = Student("inshrah" , 57)

# s1.display()

from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class CAT(Animal):
    def sound(self):
        return "meow"

class DOG(Animal):
    def sound(self):
        return "bark"

object1 = CAT()
object2 = DOG()

print(object1.sound())
print(object2.sound())


#student class

class Student :
    def __init__(self, name , grades):
        self.name = name
        self.grades = grades
    
    def get_information(self):
        print(f"name: {self.name},")
        