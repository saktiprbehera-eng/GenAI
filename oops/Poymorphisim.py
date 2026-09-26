## Base Class
import math


class Animal:
    def speak(self):
        return "Sound of the animal"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())


### Polymerphisim with Function and methods
## Base Class

class Shape:
    def area(self):
        return "The area of the figure"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

##Derived class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2;

## Function that demonstrates polymerphisim
def print_area(shape):
    print(f"the area is {shape.area()}")

rectangle=Rectangle(100,200)
circle=Circle(3)
print_area(rectangle)
print_area(circle)


## Polymerphisim with Abstract Base class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class MotorCycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

def start_vehicle(vehicle):
    print(vehicle.start_engine())
car=Car()
motorcycle=MotorCycle()
start_vehicle(car)
start_vehicle(motorcycle)