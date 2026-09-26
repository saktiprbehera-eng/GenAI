from prompt_toolkit.key_binding.bindings.named_commands import uppercase_word


def square(x):
    return x*x

print(square(5))

numbers = [1,2,3,4,5,6,7,8,9,10]
list1=list(map(square,numbers))
print(list1)

# using lambda
square_list=list(map(lambda x:x*x,numbers))
print(square_list)

# Map Multiple iterable
number1=[1,2,3]
number2=[4,5,6]

added_number=list(map(lambda x,y:x+y,number1,number2))
print(added_number)

str_num=['1','2','3','4','5','6','7','8','9']
int_num=list(map(int,str_num))
print(str_num)
print(int_num)

words=['apple','banana','mango']
upper_words=list(map(str.upper,words))
print(upper_words)

def get_name(person):
    return person['name']

people=[
    {'name':'sakti','age':18,'gender':'male'},
    {'name':'prasad','age':19,'gender':'male'},
    {'name':'behera','age':20,'gender':'male'},
]

print(list(map(get_name,people)))