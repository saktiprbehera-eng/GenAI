# This is a sample Python script.
from cgi import print_form


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hello World")
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

char_name = "sakti"
char_age = 30
print(char_name)
print(char_age)

# age=int(input("what is your age"))
# print(age,type(age))


for i in range(3):
    for j in range(2):
        print(f"{i} ,and j:{j}")

names = ["sakti","prasad","behera",1,2,3,4,5]
print(names)

mixedList=[1,"sakti",3.14,True]
print(mixedList)

fruits = ["apple","banana","mango","kiwi","orange"]
for fruit in fruits:
    print(fruit)

print(fruits[1])
print(fruits[1:])
print(fruits[1:3])
print(fruits[::2])

fruits.append("grape")
print(fruits)
fruits.insert(1,"tomato")
print(fruits)

popped_fruits=fruits.pop()
print("popped fruits: "+popped_fruits)

index=fruits.index("kiwi")
print(index)

fruits.reverse()
print(fruits)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::3])

#normal loop
for num in numbers:
    print(num)
#index based
for index,num in enumerate(numbers):
    print(index,num)

lst=[]
for i in range(10):
    lst.append(i**2)
print(lst)

square=[x**2 for x in range(10)]
print(square)

even_number=[x for x in range(10) if x%2==0]
print(even_number)

list1=[1,2,3,4]
list2=['a','b','c','d']
pairs=[[i,j] for i in list1 for j in list2]
print(pairs)

words=["hello","world","python","list","comprehension"]
lengths=[len(word) for word in words]
print(lengths)

#tuples
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))

list=list();
print(type(list))
tuple1=tuple();
print(type(tuple1))

numbers1=tuple([1,2,3,4,5])
print(numbers1)

mixed_tuple=(1,"Hello world",3.14,True)
print(mixed_tuple)

print(numbers1[0])
print(numbers1[-1])
print(numbers1[:4])

print(numbers1[::])
print(numbers1[::-1])

print(numbers1+mixed_tuple)

print(numbers1*2)
print(mixed_tuple*2)
lst=[1,2,3,4,5]
print(lst)
lst[1]="sakti"
print(lst)
#numbers1[1]="sakti"
#print(numbers1)

print(numbers1.count(2))
print(numbers1)
print(numbers1.index(3))

#unpacked tuples
a,b,c,d=mixed_tuple
print(a,b,c,d)

#unpack with *
numbers=(1,2,3,4,5);
first,*middle,last=numbers;
print(first,middle,last)

#nested list
lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst[0][2])

#nested tuples
tupl=((1,2,3),("a","b","c"),(True,False,True))
print(tupl[0])
print(tupl[1][2])

#iterate on tuple
for sub_tup in tupl:
    for item in sub_tup:
        print(item,end=" ")
    print()

#dictionary
empty_dict={}
print(type(empty_dict))

#2nd way to generate
empty_dict=dict()
print(type(empty_dict))

student={"name":"sakti","age":30}
print(student)
print(type(student))

student={"name":"sakti","age":30,"name":24}
print(student)
print(student["name"])

student={"name":"sakti","age":30,"grade":"A"}
print(student["age"])
print(student["grade"])
print(student)
student["address"]="india"
print(student)

#delete a data
del student["grade"]
print(student)

#dictionary methods
keys=student.keys()
print(keys)
values=student.values()
print(values)

items=student.items()
print(items)

#shallow copy
student_copy=student
print(student)
print(student_copy)

student["name"]="prasad"
print(student)
print(student_copy)

student_copy1=student.copy()
print(student)
print(student_copy1)

student["name"]="Behera"
print(student)
print(student_copy1)

#iterates in dictionary
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(f"{key}:{value}")

## Nested dictionary
students={
    "student1":{
        "name":"sakti",
        "age":30,
        "grade":"A"
    },
    "student2":{
        "name":"prasad",
        "age":32,
        "grade":"A+"
    }
}
print(students)
print(students["student1"]["name"])
print(students["student2"]["name"])

#items
print(students.items())

# Iterate over nested dictionary
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")

# dictionary comprehansive
square={x:x**2 for x in range(5)}
print(square)

#condition dictionary comprehansive
even={x:x**2 for x in range(0,10) if x%2==0}
print(even)

## Practical Example
# Frequency of element in list
list=[1,1,2,2,3,3,3,4,5,6,6,7,7,8,8,8,9,0,0]
frequency={}
for num in list:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)

#Merge 2 dictionary into 1
dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merge_dict={**dict1,**dict2}
print(merge_dict)

## Real time work
to_do_list=["Buy groceries","Clean the house","Pay bills"]

##adding to task
to_do_list.append("Schedule meeting")
to_do_list.append("Go for run")

#Remove a task
to_do_list.remove("Clean the house")

#checking the task in the list
if "Pay bills" in to_do_list:
    print("Don't forget to utility bills")

print("To do list remaining")
for task in to_do_list:
    print(f"-{task}")

#Organizing student grades
grades=[85,92,78,90,88]

grades.append(95)

#calculate the average grade
avg_grade=sum(grades)/len(grades)
print(f"Average Grade: {avg_grade:.2f}")

max_grade=max(grades)
min_grade=min(grades)
print(f"Max Grade: {max_grade}")
print(f"Min Grade: {min_grade}")

#Managing an inventory
inventory=["apple","banana","orange","mango"]

#adding new item
inventory.append("grapes")

# Removing an item that is out of stock
inventory.remove("banana")

item = "orange"
if item in inventory:
    print(f"Item is in inventory")
else:
    print(f"Item is not in inventory")

#printing the inventory
print("Inventory List:")
for item in inventory:
    print(f"-{item}")

# Collecting user feedback
feedback = ["Great service!", "Very satisfied", "Could be better", "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

# Counting specific feedback
positive_feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
print(f"Positive Feedback Count: {positive_feedback_count}")

# Printing all feedback
print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")