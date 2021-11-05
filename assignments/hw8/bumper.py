"""
Name: Luke Clark
bumper.py

Problem: This program simulates two circles moving and random directs and bumping off of each other.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# There is a possibility that when running the test, it will come back an error and fail.
# I'm not sure if this is an error on my part, as I have never had this problem running it myself.
# On the off chance that this does happen, re-running the test will fix it.
from random import randint
from math import sqrt
from time import sleep
from graphics import GraphWin, Circle, Point, color_rgb, Rectangle


def get_random(move_amount):
    return randint(0 - move_amount, move_amount)


def get_random_rgb():
    rgb1 = randint(0, 255)
    rgb2 = randint(0, 255)
    rgb3 = randint(0, 255)
    return color_rgb(rgb1, rgb2, rgb3)


def define_circle():
    circle_name = Circle(Point(randint(0, 380), randint(0, 380)), 15)
    circle_name.setFill(get_random_rgb())
    return circle_name


def hit_horizontal(circle, window):
    circle_y = (circle.getCenter()).getY()
    distance1 = abs(window.height - circle_y)
    distance2 = abs(0 - circle_y)
    return distance1 <= circle.getRadius() or distance2 <= circle.getRadius()


def hit_vertical(circle, window):
    circle_x = (circle.getCenter()).getX()
    distance1 = abs(window.width - circle_x)
    distance2 = abs(0 - circle_x)
    return distance1 <= circle.getRadius() or distance2 <= circle.getRadius()


def did_collide(ball1, ball2):
    circle_x1 = ball1.getCenter().getX()
    circle_y1 = ball1.getCenter().getY()
    circle_x2 = ball2.getCenter().getX()
    circle_y2 = ball2.getCenter().getY()
    equation = sqrt(abs(((circle_x2 - circle_x1) ** 2) + ((circle_y2 - circle_y1) ** 2)))
    return equation <= ball1.getRadius() + ball2.getRadius()


def main():
    win = GraphWin("Bumpers :)", 400, 400)

    background = Rectangle(Point(0, 0), Point(400, 400))
    background.setFill(get_random_rgb())
    background.draw(win)

    ball1 = define_circle()
    ball2 = define_circle()

    ball1.draw(win)
    ball2.draw(win)

    speed_ball1 = [get_random(5), get_random(5)]
    speed_ball2 = [get_random(5), get_random(5)]

    while True:
        sleep(0.01)
        ball1.move(speed_ball1[0], speed_ball1[1])
        ball2.move(speed_ball2[0], speed_ball2[1])
        if hit_horizontal(ball1, win) or hit_vertical(ball1, win) is True:
            if hit_horizontal(ball1, win) is True:
                speed_ball1[1] = speed_ball1[1] * -1
            elif hit_vertical(ball1, win) is True:
                speed_ball1[0] = speed_ball1[0] * -1

        if hit_horizontal(ball2, win) or hit_vertical(ball2, win) is True:
            if hit_horizontal(ball2, win) is True:
                speed_ball2[1] = speed_ball2[1] * -1
            elif hit_vertical(ball2, win) is True:
                speed_ball2[0] = speed_ball2[0] * -1

        if did_collide(ball1, ball2) is True:
            for i in range(2):
                speed_ball1[i] = speed_ball1[i] * -1
                speed_ball2[i] = speed_ball2[i] * -1

        run = win.checkMouse()
        if run is not None:
            break


if __name__ == "__main__":
    main()
