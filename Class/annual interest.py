"""
Name: Luke Clark
annual interest.py

Problem: this program calculates the value of an investment after a certain number of years

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    balance = eval(input("Input starting value: "))
    interest_rate = eval(input("Input annual interest rate: ")) / 100
    years = eval(input("Input number of years to calculate: "))
    for i in range(years):
        balance *= (interest_rate + 1)
    print("Total account value is: {}{}".format("$", round(balance, 2)))


if __name__ == "__main__":
    main()
