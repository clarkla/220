"""
Name: Luke Clark
lab13.py
"""
from graphics import *


def binary_search(search_val, values):
    mid = values[len(values) // 2]
    while (mid != search_val) and (len(values) != 1):
        if mid > search_val:
            values = values[:mid]
        else:
            values = values[mid + 1:]
        mid = values[len(values) // 2]
    if mid == search_val:
        return True
    else:
        return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for x in range(i, len(values)):
            if values[x] < lowest:
                lowest = values[x]
                pos = values.index(lowest)
        values[i], values[pos] = values[pos], values[i]
    return values


def calc_area(rect):
    height = abs(rect.getP1().getY() - rect.getP2().getY())
    width = abs(rect.getP1().getX() - rect.getP2().getX())
    return height * width


def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = d[i]
    return rectangles

def trade_alert(filename):
    file = open(filename, "r")
    data = file.read().split()
    int_data = []
    for i in data:
        int_data.append(int(i))
    seconds = 0
    for i in int_data:
        seconds += 1
        if i > 830:
            print("Alert at {} seconds (Value: {})".format(seconds, i))
        elif i > 500:
            print("Warning at {} seconds (Value: {})".format(seconds, i))


def main():
    pass
    # print(binary_search(1, [0, 1, 2, 3]))
    # print(selection_sort([5, 4, 3, 2, 1]))
    # trade_alert("trades.txt")


main()
