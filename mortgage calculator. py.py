
try:
    amount_borrowed = int(input("Hi, write your amount borrowed here to calculate"))
    annual_interest_rate = int(input("Hi, write your annual interest rate here to calculate"))
    number_of_monthly_payments = int(input("Hi, write your number of monthly payments here to calculate"))
    monthly_payment = amount_borrowed * (annual_interest_rate // 12) * ((1 + annual_interest_rate // 12) ** number_of_monthly_payments) // (((( 1 + annual_interest_rate // 12) ** number_of_monthly_payments) - 1)) if amount_borrowed != 0 or annual_interest_rate != 0 or number_of_monthly_payments != 0 else 0
except ZeroDivisionError:
    monthly_payment = 0
print(monthly_payment) 
