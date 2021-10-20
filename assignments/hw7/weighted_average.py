"""
Name: Luke Clark
weighted_average.py

Problem: This program calculates student's grades from an input file and writes
them to an output file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# weighted average(input, output)
# Output each student's average and output overall class average
# If the weight for students do not add up to 100, output that it is too high/low
# input file will be grades.txt
# output file will be avg.txt


def weighted_average():
    in_file_name = "grades.txt"
    file = open(in_file_name, "r")
    averages = []
    for i in file:
        list1 = i.split(":")
        names_list = list1[0]
        number_list = list1[1].split()
        number_list[0] = 1

"""
        weight_total = 0
        for weight in numbers[::2]:
            print(weight)
            weight_total += weight
        # if weight_total == 100:
"""

