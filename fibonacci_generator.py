# TASK 1: FIBONACCI GENERATOR (Using Recursion)
# The Fibonacci series is a sequence where each number is the sum of the two preceding numbers, 
# defined by a mathematical recurrence relationship.
# Implement a Python program to generate the Fibonacci series using a recursive function.

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
for i in range(1, num + 1):
    print(fibonacci(i), end=" ")
