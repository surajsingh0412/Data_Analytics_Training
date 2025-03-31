#Write a Python program to reverse a number using a while loop.


def reverse_number(n):
    reversed_num = 0
    while n > 0:
        remainder = n % 10
        reversed_num = (reversed_num * 10) + remainder
        n = n // 10  
    return reversed_num
num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))



#Write a Python program to check whether a number is a palindrome or not.

number = 425
store = number
ans = 0
while(number):
    remainder = number % 10
    ans = ans * 10 + remainder
    number = number // 10
if(ans == store):
    print("Palindrome") 
else:
    print("Not Palindrome")



#Write a Python program to find the factorial of a given number using a while loop.

def factorial(n):
    result = 1  
    if n < 0:
        return "Factorial is not defined for negative numbers"
    while n > 0:
        result *= n  
        n -= 1  
    return result
num = int(input("Enter a number: "))
print(f"The factorial of {num} is: {factorial(num)}")


# Accept numbers using the input() function until the user enters 0. If the user inputs 0, then break the while loop and display the sum of all the numbers.

sum = 0
while True:
    number = int(input("Enter the Number:"))
    if(number == 0):
        break
    sum = sum + number
print(sum)
