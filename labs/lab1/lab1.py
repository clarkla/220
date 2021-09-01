"""
Name: Luke Clark
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area = ", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the total shots taken: "))
    shots_made = eval(input("Enter the total shots made: "))
    percentage = (shots_made / total_shots * 100)
    print("Percentage: ", percentage)


def coffee():
    price_per_lb = 10.50
    shipping_per_lb = 0.86
    fixed_cost = 1.50
    lbs = eval(input("Enter number of pounds of coffee ordered: "))
    cost = price_per_lb * lbs + shipping_per_lb * lbs + fixed_cost
    print("Total cost is: ", cost)


def kilometers_to_miles():
    mi_per_km = 1.61
    kilometers = eval(input("Enter number of kilometers: "))
    miles = kilometers / mi_per_km
    print(miles, "miles")


# calc_area()

# calc_volume()

# shooting_percentage()

# coffee()

# kilometers_to_miles()
