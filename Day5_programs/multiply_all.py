#  Multiplies Element In A List
# Multiply_All: Write a function that multiplies all the numbers in a list and returns the same. The list comes as an input argument.

# For example : multiply_all([10,2,3]), should returns 60

# Input => Original List : [10, 2, 3]

# Output =>

# Original List : [10, 2, 3]
# Result After Multiplying Elements In The List : 60


####################
def multiply_all(numbers):
    result = 1  # Initialize result to 1 (since 1 is the multiplicative identity)
    for num in numbers:
        result *= num  # Multiply each number with result
    return result

# Example usage
num=int(input("Enter the value for list : "))
numbers = []
for i in range (num):
  ele = int(input("Enter the number : "))
  numbers.append(ele)

print(f"Original List : {numbers}")
print(f"Result After Multiplying Elements In The List : {multiply_all(numbers)}")
