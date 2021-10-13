"""
Name: Luke Clark
lab7.py
"""

import math


def cash_conversion():
    value = eval(input("Enter value: "))
    print("${:.2f}".format(value))


def encode():
    message = input("Enter message: ")
    key = eval(input("Enter key: "))
    for i in message:
        shift = ord(i) + key
        print(chr(shift), end="")


def sphere(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area


def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


def sum_n(n):
    acc = 0
    for i in range(1, n + 1):
        acc += i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(1, n + 1):
        acc += i ** 3
    return acc


def encode_better():
    message = input("Enter message: ")
    key = input("Enter key: ")
    for i in range(len(message)):
        shift = (ord(message[i]) + ord(key[i]) - 97)
        print(chr(shift), end="")


def main():
    # cash_conversion()
    # encode()
    # print(sphere(3))
    # print(sphere_volume(3))
    # print(sum_n(3))
    # print(sum_n_cubes(3))
    # encode_better()
    pass


main()
