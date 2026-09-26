## Functional Examples
import re


# Example 1: Temperature Conversion

def convert_temperature(temp,unit):
    """This function converts temperature in celsius to fahrenheit and vicecersa"""
    if unit == "C":
        return temp * 9 / 5 + 32 ## Celsius to Farnhite
    elif unit == "F":
        return (temp-32) * 5/9
    else:
        return None

print(convert_temperature(25,"C"))
print(convert_temperature(77,"F"))

# Example 2: Password Strength
def password_strength(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+'for char in password):
        return False
    return True
## Calling Function
print(password_strength("Sakti@890"))
print(password_strength("WeakPassword"))


#Example 3: Calculate the total cost of item in a shopping cart

def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item["price"]*item["quantity"]
    return total_cost

cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3},
]
print(calculate_total_cost(cart))

#Example 4: string is palindrom
def isPalindrom(s):
    s=s.lower().replace(" ","")
    return s == s[::-1]

print(isPalindrom("madam"))
print(isPalindrom("A man a plan a canal Panama"))
print(isPalindrom("banana"))

# Example 5: Factorial of a number using recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))

#Example 6: A function read a file  and count the frequency of each word
def count_word_frequency(file_path):
    word_frequency = {}
    with open(file_path,'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word=word.lower().strip('.,!?;:"\'')
                word_frequency[word] = word_frequency.get(word,0)+1

    return word_frequency
file_path="sample.txt"
word_frequency = count_word_frequency(file_path)
print(word_frequency)

#Example 7: Validate email address
def validateEmail(email):
    pattern= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern,email) is not None
print(validateEmail("text@emaple.com"))
print(validateEmail("invalid-email"))