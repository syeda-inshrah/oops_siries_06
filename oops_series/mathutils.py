import random

class Mathutils:
    @staticmethod
    def add (a,b):
        return a + b 


a = random.randint(1 , 99)
b = random.randint(1 , 99)

print(Mathutils.add(a , b))