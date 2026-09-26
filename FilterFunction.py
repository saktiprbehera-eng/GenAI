import math


def even(num):
    if num%2==0:
        return True
even(50)

lst = list((1,2,3,4,5,6,7,8,9,10,12,11));

print(list(filter(even,lst)));

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
greater_than5=list(filter(lambda x:x>5,numbers));
print(greater_than5);


numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_greater_than5=list(filter(lambda x:x>5 and x%2==0,numbers));
print(even_greater_than5);

people=[
    {'name':'sakti','age':25},
    {'name':'suresh','age':20},
    {'name':'hari','age':35}
]

def age_greater_than25(person):
    return person['age']>=25
print(list(filter(age_greater_than25,people)))

math.sqrt(16)