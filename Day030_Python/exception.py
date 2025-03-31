# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero! Please enter a non-zero denominator.")
    except ValueError:
        print("Error: Please enter valid numbers.")
divide_numbers()



# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. 

def get_integer_input():
    try:
        user_input = input("Please enter an integer: ")
        integer_value = int(user_input)  
        print(f"You entered the integer: {integer_value}")
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
get_integer_input()



# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

def open_file():
    try:
        filename = input("Enter the name of the file to open: ")
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")
open_file()


# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.   

def get_numbers():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        num1 = float(num1)
        num2 = float(num2)
        print(f"The sum of {num1} and {num2} is: {num1 + num2}")
    except ValueError:
        print("Error: Invalid input! Both inputs must be numbers.")
        raise TypeError("Both inputs must be numeric values.")
get_numbers()
