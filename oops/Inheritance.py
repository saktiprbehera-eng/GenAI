## Inheritance
## Parent class

class Car:
    def __init__(self, window, doors, engineType):
        self.window = window
        self.doors = doors
        self.engineType = engineType

    def drive(self):
        print(f"The Person will drive the {self.engineType} car")

car1=Car(4,5,"petrol")
print(car1.drive())


class Tesla(Car):
    def __init__(self, window, doors, engineType,is_selfDriving):
        super().__init__(window,doors,engineType)
        self.is_selfDriving = is_selfDriving

    def selfDriving(self):
        print(f"Tesla supports self driving: {self.is_selfDriving}")

tesla1=Tesla(4,5,"Electric",True)
print(tesla1.selfDriving())


## Multiple Interitance
## when a class inherit more than one base class

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Sub class must implement this method")

class Pet:
    def __init__(self, owner):
        self.owner = owner

## Derived class

class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    def speak(self):
        return f"{self.name} say woof"

# create an object
dog=Dog("Buddy","Sakti")
print(dog.speak())
print(f"Owner is {dog.owner}")