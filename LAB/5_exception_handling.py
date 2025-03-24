# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
# input).
#  Write a Python program to demonstrate handling multiple exceptions.

try:
    num1=int(input('Enter your 1st number: '))
    num2=int(input('Enter your 2nd number : '))

    result=num1/num2

    print("Result:", result)

except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
except ValueError:
        print("Error: Invalid input. Please enter numeric values.")