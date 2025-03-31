# Print the first 10 natural numbers using a for loop.

for i in range(1, 11):  
    print(i)


# Python program to check if the given string is a palindrome.

def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')



#Python program to check if a given number is an Armstrong number.

number = int(input("Enter a number: "))
total = 0
temp = number
while temp > 0:
    digit = temp % 10
    total = total + digit * digit * digit  
    temp //= 10
if total == number:
    print(f"{number} is a armstromg number")
else:
    print(f"{number} is not Armstrong number.")



# Python program to get the Fibonacci series between 0 to 50.

def fibonacci(number):
    a, b = 0, 1
    while a <= number:
        print(a, end=" ")
        a, b = b, a + b
fibonacci(50)


# Python program to check the validity of password input by users.

import re  
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@#$%^&+=]', password):
        return False
    return True
password = input("Enter a password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must be at least 8 characters long, "
          "contain at least one uppercase letter, one lowercase letter, "
          "one digit, and one special character.")
