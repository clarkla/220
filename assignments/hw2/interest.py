"""
Name: Luke Clark
interest.py

Problem: This program calculates monthly interest.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    annual_interest_rate = eval(input("Input annual interest rate: ")) / 100
    billing_cycle = eval(input("Input total number of days in billing cycle: "))
    previous_balance = eval(input("Input previous net balance: "))
    payment_amount = eval(input("Input payment amount: "))
    day_paid = eval(input("Input how many days into billing cycle payment was made: "))
    days_left = billing_cycle - day_paid
    monthly_interest_rate = annual_interest_rate / 12
    step_1 = previous_balance * billing_cycle
    step_2 = payment_amount * days_left
    step_3 = step_1 - step_2
    average_daily_balance = step_3 / billing_cycle
    monthly_interest_charge = round(average_daily_balance * monthly_interest_rate, 2)
    print(monthly_interest_charge)


if __name__ == "__main__":
    main()
