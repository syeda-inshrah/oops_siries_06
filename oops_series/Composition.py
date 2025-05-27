# Engine class
class Engine:
    def start(self):
        return "Engine started."

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Engine object passed to Car

    def start_car(self):
        return self.engine.start()  # Accessing Engine method

# Example usage
my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_car())
