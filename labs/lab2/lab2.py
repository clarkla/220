"""
Name: Luke Clark
lab2.py
"""
import math


def sum_of_threes():
    bound = eval(input("Input upper bound: "))
    acc = 0
    for acc in range(0, bound + 1, 3):
        print(acc)


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l, end=" ")
        print()


def triangle_area():
    a = eval(input("Input length of side a: "))
    b = eval(input("Input length of side b: "))
    c = eval(input("Input length of side c: "))
    s = (a + b + c) / 2
    x = s * (s - a) * (s - b) * (s - c)
    print(math.sqrt(x))


def sum_squares():
    lower_range = eval(input("Input lower range: "))
    upper_range = eval(input("Input upper range: "))
    acc = 0
    for i in range(lower_range, upper_range + 1):
        acc += i ** 2
    print(acc)


def power():
    number = eval(input("Input number: "))
    exponent = eval(input("Input exponent: "))
    acc = number
    for i in range(exponent-1):
        acc *= number
    print(number, "^", exponent, "=", acc)

