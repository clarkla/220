"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    white = Circle(Point(250, 250), 500 / 2)
    white.setFill("white")
    white.draw(win)
    black = Circle(Point(250, 250), 500 / 2.5)
    black.setFill("black")
    black.draw(win)
    blue = Circle(Point(250, 250), 500 / 3.33)
    blue.setFill("blue")
    blue.draw(win)
    red = Circle(Point(250, 250), 500 / 5)
    red.setFill("red")
    red.draw(win)
    yellow = Circle(Point(250, 250), 500 / 10)
    yellow.setFill("yellow")
    yellow.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    shape = Polygon(p1, p2, p3)
    shape.draw(win)

    dx1 = abs(p2.getX() - p1.getX()) ** 2
    dy1 = abs(p2.getY() - p1.getY()) ** 2
    dx2 = abs(p3.getX() - p1.getX()) ** 2
    dy2 = abs(p3.getY() - p1.getY()) ** 2
    dx3 = abs(p3.getX() - p2.getX()) ** 2
    dy3 = abs(p3.getY() - p2.getY()) ** 2
    length1 = math.sqrt(dx1 + dy1)
    length2 = math.sqrt(dx2 + dy2)
    length3 = math.sqrt(dx3 + dy3)

    perimeter = length1 + length2 + length3
    s = perimeter / 2
    area = math.sqrt(s * ((s - length1) * (s - length2) * (s - length3)))

    perimeter_text = Text(Point(250, 20), "Perimeter= " + str(round(perimeter, 2)))
    perimeter_text.draw(win)
    area_text = Text(Point(250, 40), "Area= " + str(round(area, 2)))
    area_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_entry = Entry(Point(win_width / 2, win_height / 2 + 40), 3)
    red_entry.setTextColor("red")
    red_entry.draw(win)
    green_entry = Entry(Point(win_width / 2, win_height / 2 + 70), 3)
    green_entry.setTextColor("green")
    green_entry.draw(win)
    blue_entry = Entry(Point(win_width / 2, win_height / 2 + 100), 3)
    blue_entry.setTextColor("blue")
    blue_entry.draw(win)

    for i in range(5):
        win.getMouse()
        shape.setFill(color_rgb(int(red_entry.getText()), int(green_entry.getText()), int(blue_entry.getText())))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("Enter string: ")
    print(string[0])
    print(string[-1])
    print(string[2:6])
    print(string[0] + string[-1])
    print(string[0:3] * 10)
    for i in string:
        print(i)
    print(len(string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = x[0] + x[1] + x[2]
    print(x)
    x = len(values)
    print(x)


def another_series():
    terms = eval(input("Enter number of terms: "))
    acc = 0
    for i in range(0, terms):
        y = 2 + (2 * (i % 3))
        acc += y
        print(y, end=" ")
    print("\nsum = " + str(acc))


def main():
    target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()


main()
