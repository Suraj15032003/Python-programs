# Develop a function to compute average from a given list of numbers and to return the same.

# Input => List of numbers Ex. [10, 20, 30, 40, 50]

# # Output => Average of the List is 30.0

###############

def compute_avg(list_num , n):
  total_of_list =sum(list_num)
 # len_list =len(list_num)
  avg_list=total_of_list/n#len_list
  if n==0:
    return 0
  else:
    return avg_list
n =int(input("Enter the number of elements : "))
numbers = []
for i in range(n):
  element = int(input("Enter element : "))
numbers.append(element)

avg_of_list=compute_avg(numbers , n)
print(f"Average of the List is {avg_of_list}")