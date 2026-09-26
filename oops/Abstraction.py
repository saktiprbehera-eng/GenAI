from abc import ABC,abstractmethod

## Abstract Base class
class Vehicle(ABC):
    def drive(self):
        print("Driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        print("Car engine started")

def operate_vehicle(vehicle):
    vehicle.start_engine()

car=Car()
operate_vehicle(car)