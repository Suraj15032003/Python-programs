# Car_Loan: Write a function CarLoan payment computation. This function takes three arguments - P(Principal Loan Amount), Y(years to pay off) and R (percent interest compounded monthly) and it returns the monthly payment amount.

# The formula is:

# Loan Formula

# Purpose - The purpose of this program is to pass the arguments to the function

# Input => 20000, 5, 5

# Output => Monthly car loan payment: 377.42

#####################################


def cal_car_loan_payment(P, Y, R):
    r = R / 100 / 12  # Convert annual interest rate to monthly decimal rate
    n = Y * 12  # Convert years to months
    monthly_payment = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return monthly_payment

principal_amount = float(input("Enter the principal loan amount in rupees: "))
years_to_pay_off = float(input("Enter the duration to pay off the loan in years: "))
annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))

monthly_payment = cal_car_loan_payment(principal_amount, years_to_pay_off, annual_interest_rate)
print(f"Monthly car loan payment: {monthly_payment:.2f}")
