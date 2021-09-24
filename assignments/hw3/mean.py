"""
Name: Luke Clark
mean.py

Problem: This program calculates the RMS Average, Harmonic Mean,
and the Geometric Mean of a set of numbers.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# Note: It has since come to my attention that this assignment was entirely do-able
# without the use of a list. The original solution I came up with I didn't even consider
# the possibility of not using something like a list. If going ahead and learning some
# about lists and how to use them is something I shouldn't have done, I can rewrite this.

# Take input from user to determine how many numbers will be used
# Take input from user to determine what numbers will be used
# Output RMS Average, Harmonic Mean, and Geometric Mean of numbers

# User will input number for how many inputs are required
# A list will be created
# A for loop using range based on original user input will add user inputs to list
# Three for loops will be created using the list, one to calculate each formula
# Each for loop will use an accumulator in order to calculate the output
# Print output (accumulator) of each for loop, each on a separate line
# Round output to 3 decimal places

import math


def main():
    # Total amount of numbers to be used
    total = eval(input("Input amount of numbers to be calculated: "))

    # Create a list and append user input to it
    numbers = []
    for i in range(1, total + 1):
        next_number = eval(input("Input value " + str(i) + ": "))
        numbers.append(next_number)

    # RMS average formula and output
    rms_average = 0
    for i in numbers:
        rms_average += i ** 2
    rms_average /= total
    rms_average = math.sqrt(rms_average)
    print(round(rms_average, 3))

    # Harmonic mean formula and output
    harmonic_mean = 0
    for i in numbers:
        harmonic_mean += 1 / i
    harmonic_mean = total / harmonic_mean
    print(round(harmonic_mean, 3))

    # Geometric mean formula and output
    geometric_mean = 1
    for i in numbers:
        geometric_mean *= i
    geometric_mean = geometric_mean ** (1 / total)
    print(round(geometric_mean, 3))


if __name__ == "__main__":
    main()
