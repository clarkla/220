"""
Name: Luke Clark
lab9.py
"""
from graphics import *
import math


def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in nums:
        acc += i
    return acc


def toNumbers(nums):
    for i in range(len(nums)):
        nums[i] = int(nums[i])


def writeSumOfSquares():
    in_file = open(input("Input file: "), "r")
    out_file = open(input("Output file: "), "w")
    for i in in_file:
        list1 = i.split()
        toNumbers(list1)
        squareEach(list1)
        print("Sum of squares = " + str(sumList(list1)), file=out_file)


def starter():
    weight = float(input("PLease enter weight so I can go home: "))
    numWins = int(input("Now enter number of wins or so help me god: "))
    if 150 <= weight < 160 and numWins >= 5:
        print("THIS LUCKY INDIVIDUAL IS A STARTER :D")
    elif weight > 199 or numWins > 20:
        print("WOW, HE CAN START! :)")
    else:
        print("leave.")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def circlesOverlap():
    win = GraphWin("Cirgle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt(((p2.getX() - p1.getX()) ** 2) + ((p2.getY() - p1.getY()) ** 2))
    circle1 = Circle(p1, radius1)
    circle1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt(((p4.getX() - p3.getX()) ** 2) + ((p4.getY() - p3.getY()) ** 2))
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    if math.sqrt(((p3.getX() - p1.getX()) ** 2) + ((p3.getY() - p1.getY()) ** 2)) < radius1 + radius2:
        print("Holy cow! The circles are overlapping!!")
    else:
        print("Circles are following recommended pandemic guidelines.")
    win.getMouse()
    win.close()


def main():
    # print(sumList([1, 2, 3]))
    # writeSumOfSquares()
    # starter()
    # print(leapYear(2000))
    circlesOverlap()


main()
