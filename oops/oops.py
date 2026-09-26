class Car:
    pass
audi=Car()
bmw=Car()

print(type(audi))

print(audi)
print(bmw)

audi.windows=4
print(audi.windows)
tata=Car()
tata.doors=4
#print(tata.windows)

#Instance variable and methods
class Dog:
    ## Constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

## create objects
dog1=Dog("buddy",3)
print(dog1)
print(dog1.name)
print(dog1.age)

dog2=Dog("Lucy",4)
print(dog2)
print(dog2.name)
print(dog2.age)

#Define a class with instance methods
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def meow(self):
        print(f"{self.name} is meow.")

cat1=Cat("daemon",5)
cat1.meow()

## Modeling a Bank account
## Define a class for Bank
class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} amount is deposited. New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient fund!")
        else:
            self.balance-=amount
            print(f"{amount} amount is withdrawn. New balance is {self.balance}")

    def get_balance(self):
        return self.balance

## create an object
account = BankAccount("Sakti",5000)
print(account.get_balance())

## call instance methods
account.deposit(100)
account.withdraw(300)
print(account.get_balance())