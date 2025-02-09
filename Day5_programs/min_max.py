# Develop a function to compute minimum as well as maximum from a list of numbers. Function takes number list as input argument and returns both max and min.

# Input => num_list = [10, 5, 20, 15, 30]

# Output =>

# Original List : [10, 5, 20, 15, 30]
# Minimum number in a List is  5
# Maximum number in a List is  30

def compute_min_max(num_list):
  min_num = min(num_list)
  max_num = max(num_list)
  return min_num , max_num

len_list = int(input("Enter the length of the list"))
num_list=[]
for i in range (len_list):
  number = int(input("Enter the number: "))
  num_list.append(number)

min_value , max_value = compute_min_max(num_list)
print(f"Minimum number in a List is {min_value}")
print(f"Maximum number in a List is {max_value}")
