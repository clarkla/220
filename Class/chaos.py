"""
Name: Luke Clark
chaos.py

Problem: this program illustrates a chaotic function

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)


main()
