# Count Down using Recursion
# Write a function in a recursive way which takes n as input and prints n, n-1, n-2 , …0.

# For example if n =3, it will print 3 2 1 0

# Input => Enter the number to print the count down: 3

# Output =>

# Enter the number to print the count down: 3
# 3
# 2
# 1
# 0

######################3

def count_down(num):
  if num<0:
    return
  print(num)
    
  count_down(num-1)

num = int(input("Enter the number to print count down : "))
count_down(num)