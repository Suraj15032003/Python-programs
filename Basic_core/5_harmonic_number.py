num = int(input("Enter the value of n: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    harmonic_sum = 0.0

    for i in range(1, num + 1):
        harmonic_sum += 1 / i  # Add the reciprocal of i

    print(f"The {num}th Harmonic Number is: {harmonic_sum:.4f}")  # Limit to 4 decimal places
