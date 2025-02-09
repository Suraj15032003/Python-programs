num =int(input("Enter the value of n"))
i=0
counter=1
while(i<num):
    i=2**counter
#If i is still less than num, it prints i
    if(i<num):
       print(i)
    counter+=1
