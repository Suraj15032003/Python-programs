# Calculator: Develop a basic calculator program which takes a symbol for the computation to be performed like ‘+’, ‘-’, ‘*’ , OR ‘%’ and two input numbers as an argument.

# This function returns the result of the computation. Test this function for different computations and different input numbers. Input numbers can be float or int.

# Input =>

# Enter the symbol for the computation (+, -, *, /): +

# Enter the first number: 2

# Enter the second number: 5

# Output =>

# Enter the symbol for the computation (+, -, *, /): +
# Enter the first number: 2
# Enter the second number: 5
# Result: 7.0

##################
def calculator(symbol, num1, num2):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2
    elif symbol == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation symbol!"

# Taking user input
symbol = input("Enter the symbol for the computation (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function and displaying the result
result = calculator(symbol, num1, num2)
print(f"Result: {result}")
