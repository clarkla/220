"""
Name: Luke Clark
lab4.py
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to create rectangles")
    instructions.draw(win)

    # builds a rectangle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to make more rectangles
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of rectangle

        # new rectangle is distance from center of rectangle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        copy = shape.clone()
        shape = copy
        copy.move(dx, dy)
        copy.draw(win)

    instructions.undraw()
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width_window = 400
    height_window = 400
    win = GraphWin("Lab 4", width_window, height_window)

    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    point2.draw(win)
    shape = Rectangle(point1, point2)
    shape.draw(win)

    length = abs(point2.getX() - point1.getX())
    width = abs(point2.getY() - point1.getY())
    perimeter = 2 * (length + width)
    area = length * width

    perimeter_pt = Point(width_window / 2, height_window - 30)
    area_pt = Point(width_window / 2, height_window - 10)
    inst_pt = Point(width_window / 2, height_window - 380)
    perimeter_text = Text(perimeter_pt, "Perimeter: " + str(perimeter))
    area_text = Text(area_pt, "Area: " + str(area))
    inst_text = Text(inst_pt, "Click again to quit")

    perimeter_text.draw(win)
    area_text.draw(win)
    inst_text.draw(win)

    win.getMouse()


def circle():
    width_window = 400
    height_window = 400
    win = GraphWin("Lab 4", width_window, height_window)

    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    x = (point2.getX() - point1.getX()) ** 2
    y = (point2.getY() - point1.getY()) ** 2
    radius = math.sqrt(x + y)
    shape = Circle(point1, radius)
    shape.draw(win)

    radius_pt = Point(width_window / 2, height_window - 20)
    inst_pt = Point(width_window / 2, height_window - 380)

    radius_text = Text(radius_pt, "Radius: " + str(round(radius, 2)))
    inst_text = Text(inst_pt, "Click again to quit")

    radius_text.draw(win)
    inst_text.draw(win)

    win.getMouse()


def pi2():
    terms = eval(input("Enter the number of total terms to output: "))
    denominator = 1
    total = 0
    for i in range(1, terms + 1):
        total += 4 / denominator
        denominator += 2
        total -= 4 / denominator
        denominator += 2
    print(total)


def main():
    squares()
    # rectangle()
    # circle()
    # pi2()


main()
