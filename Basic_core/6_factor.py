N = int(input("Enter a number: "))
print("Prime factors:", end=" ")

i = 2
while i * i <= N:
    while N % i == 0:
        print(i, end=" ")
        N //= i
    i += 1

if N > 1:
    print(N)  # If there's any prime factor greater than sqrt(N)