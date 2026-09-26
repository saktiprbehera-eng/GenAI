# syntax
#lambda argument: expression

def addition1(a,b):return a+b
print(addition1(2,3))

addition=lambda a,b: a+b
print(type(addition))
print(addition(5,3))

even1=lambda a:a%2==0
print(even1(5))
print(even1(128740))

addition2=lambda a,b,c: a+b+c
print(addition2(5,3,4))

numbers=[1,2,3,4,5]
def square(num):
    return num*num
print(square(2))

## map - applies a function to all items in list
print(list(map(lambda x:x*x,numbers)))