# Reverse a string using a for loop in Python.
def reverse_string(input_str):
    rev_str = ""
    for char in input_str:
        print(char)
        rev_str = char + rev_str 
    return rev_str

original_str = "Hello, World!"
reversed_str = reverse_string(original_str)

print("Original String:", original_str)
print("Reversed String:", reversed_str)

#Write a Python program to find the sum of all 
#numbers in a list using a for loop.

def sum_of_numbers(num_list):
    total_sum = 0
    for num in num_list:
        total_sum += num
    return total_sum

numbers = [19, 87, 22, 9, 35]
result = sum_of_numbers(numbers)

print("List of Numbers:", numbers)
print("Sum of Numbers:", result)


#Write a Python program that checks whether a 
#given number is even or odd using an if-else statement.

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

user_input = int(input("Enter a number: "))
check_even_odd(user_input)


#Implement a program to determine if a year is a leap year 
#or not using if-elif-else statements.

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f"{year} is a leap year.")
    elif year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

user_input = int(input("Enter a year: "))
is_leap_year(user_input)

#Use a lambda function to square each element in a list

numbers = [4, 21, 43, 77]
squared_numbers = list(map(lambda x: x**2, numbers))

print("Original List:", numbers)
print("Squared List:", squared_numbers)

#Write a lambda function to calculate the product of two

product = lambda x, y: x * y

num1 = 3
num2 = 5
result = product(num1, num2)

print(f"The product of {num1} and {num2} is: {result}")

