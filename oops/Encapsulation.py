## Encapsulation
## Public,Protected,private and variables
from MapFunction import get_name


class Person:
    def __init__(self, name, age, gender):
        # self.name = name #public variable
        # self.age = age  #Public variable
        self.__name = name
        self.__age = age
        self.gender = gender
person = Person("sakti",30,"Male")
# print(person.name)
# print(person.age)

print(dir(person))

#get_name(person)

class Employee:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_gender(self):
        return self.__gender
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        if(age > 0):
            self.__age = age
        else:
            self.__age = 0
    def set_gender(self, gender):
        self.__gender = gender

emp=Employee("sakti",30,"Male")
print(emp.get_name())
print(emp.get_age())
print(emp.get_gender())

emp.set_name("prasad")
print(emp.get_name())
print(emp.get_age())