"""
Name: Luke Clark
lab3.py
"""


def average():
    number_of_grades = eval(input("Enter the number of grades to average: "))
    total = 0
    for i in range(1, number_of_grades + 1):
        total += eval(input("Enter your grade on HW " + str(i)))
    avg = total / number_of_grades
    print("Average is: ", avg)


def tip_jar():
    jar = 0
    for i in range(1, 6):
        jar += eval(input("Enter amount for donation " + str(i)))
    print(jar)


def newton():
    x = eval(input("Enter the number to find the square root of: "))
    refine = eval(input("Enter the number of times to refine the square root: "))
    approx = x / 2
    for i in range(refine):
        approx = (approx + (x / approx)) / 2
    print(approx)


def sequence():
    terms = eval(input("Enter the number of total terms to output: "))
    for i in range(1, terms + 1):
        print(1 + ((i // 2) * 2))


def pi():
    terms = eval(input("Enter number of terms to approximate pi: "))
    acc = 1
    for i in range(terms):
        numerator = (2 + ((i // 2) * 2))
        denominator = (1 + (((i+1) // 2) * 2))
        acc *= numerator / denominator
    print(acc * 2)
