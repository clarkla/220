"""
Name: Luke Clark
greeting.py

Problem: This programs displays a greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from time import sleep
from graphics import GraphWin, Image, Point, Text, Rectangle

win = GraphWin("Greetings", 400, 400)


def heart_arrow():
    heart = Image(Point(200, 200), "heart.png")
    heart.draw(win)
    arrow = Image(Point(810, -400), "arrow.png")
    arrow.draw(win)
    hear_blocker = Image(Point(200, 200), "heart blocker.png")
    hear_blocker.draw(win)
    instructions1 = Text(Point(200, 370), "Click to Shoot Arrow")
    instructions1.setSize(15)
    # instructions1.setTextColor("white")
    instructions1.draw(win)
    win.getMouse()
    for _ in range(580):
        arrow.move(-1, 1)
    instructions1.undraw()


def hearts():
    xacc = 20
    yacc = 25
    for _ in range(10):
        for _ in range(9):
            heart = Image(Point(xacc, yacc), "small heart.png")
            heart.draw(win)
            xacc += 45
        yacc += 40
        xacc = 20
        sleep(0.01)


def card():
    background = Rectangle(Point(0, 0), Point(400, 400))
    background.setFill("red")
    background.draw(win)
    greeting1 = Text(Point(200, 170), "Happy Valentine's")
    greeting1.setSize(20)
    greeting1.setTextColor("white")
    greeting2 = Text(Point(200, 210), "Day!")
    greeting2.setSize(20)
    greeting2.setTextColor("white")
    instructions2 = Text(Point(200, 370), "Click Window Again to Close")
    instructions2.setSize(12)
    instructions2.setTextColor("white")
    instructions2.draw(win)
    click = win.checkMouse()
    while click is None:
        sleep(0.5)
        greeting1.draw(win)
        greeting2.draw(win)
        click = win.checkMouse()
        sleep(0.5)
        greeting1.undraw()
        greeting2.undraw()


def main():
    heart_arrow()
    sleep(0.5)
    hearts()
    sleep(0.5)
    card()


if __name__ == '__main__':
    main()
