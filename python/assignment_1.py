"""Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen. 
"""

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

print("Addition: ", num_1 + num_2)
print("Subtraction: ", num_1 - num_2)
print("Multiplication: ", num_1 * num_2)
print("Division: ", num_1 / num_2)

###################################################

"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {first_name + ' ' + last_name}! Welcome to the Python program.")
