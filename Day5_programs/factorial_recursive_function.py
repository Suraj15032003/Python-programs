# PROG 5: Recursive Function
# Factorial Recursive Function: Write a factorial function in a recursive way.

# Factorial takes input as n and returns factorial of n

# Input => Enter the number to find the factorial : 5

# Output =>

# Enter the number to find the factorial : 5
# Factorial of 5 is: 120



def factorial (num):
  if num == 0 :
    return 1
  else:
    return num * factorial(num -1)

number = int(input("Enter the number to find factorial : "))
result = factorial(number)
print(f"Factorial of {number} is {result}")