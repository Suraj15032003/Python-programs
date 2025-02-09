year = int(input("Enter the year :"))
if year<1000:
    year = int(input("Enter the year again "))

if year%4==0:
    print("Its a leap year")