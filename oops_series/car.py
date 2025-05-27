class Car:
    def __init__(self , brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is starting")

c1 = Car("toyoto")
print(c1.brand)
c1.start()