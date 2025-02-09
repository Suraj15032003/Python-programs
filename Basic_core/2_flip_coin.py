import random

#taking the input of n how many times i have to flip the coin 
flip = int(input("Enter the number of times i have to flip the coin :"))

head =0
tail =0

# now storing the  random genrated input in num to calculate the percentage
for i in range(flip):
    num =random.randint(0,1)
    if num==0:
        head=head+1
    else:
        tail=tail+1

head_percentage = (head / flip) * 100
print("this is the head percentage :",head_percentage)

tail_percentage = (tail / flip) * 100
print("this is the tail percentage :",tail_percentage)

