#a=b


lst=[1,2,3,4]
lst.remove(1)
lst.pop()
print(lst)
try:
    a=b
except NameError as e:
    print(e)

try:
    result=1/2
    a=b
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

try:
    num=int(input("enter a number"))
    result=10/num
except ValueError as e:
    print("This is not a valid number")
except ZeroDivisionError as e:
    print("Please enter denominator greater than 0")
except Exception as e:
    print(e)

#try,except,else block
try:
    num = int(input("enter a number"))
    result = 10 / num
except ValueError as e:
    print(f"This is not a valid number:{e}")
except ZeroDivisionError as e:
    print("Please enter denominator greater than 0")
except Exception as e:
    print(e)
else:
    print(f"the reslt is {result}")
finally:
    print("The execution completed")


try:
    file=open("../file.txt", "r")
    content=file.read()
    a=b
    print(content)

except FileNotFoundError as e:
    print("File does not exist")
except Exception as e:
    print(e)
finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print("File closed")