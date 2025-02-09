# Power Of Number
# Write a Python function to calculate the power of a number. The function should take two parameters - the base and the exponent. Test the function with different base and exponent values.

# Input =>

# Enter the Base Number : 2

# Enter the Exponent Number : 3

# Output =>

# Enter the Base Number : 2
# Enter the Exponent Number : 3
# 2 raised to the power of 3 is: 8

#######################

def power_of_number(base, exponent):
    return base ** exponent 

base = int(input("Enter the Base Number: "))
exponent = int(input("Enter the Exponent Number: "))
result =int(power_of_number(base, exponent))# Calculating power

print(f"{base} raised to the power of {exponent} is: {result}")
