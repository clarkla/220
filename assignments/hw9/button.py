"""
Name: Luke Clark
button.py

Problem: This file creates a button class to be used by the three door game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text


class Button:
    """Packages given shape into a button object with a label"""
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x_range = range(int(self.shape.getP1().getX()), int(self.shape.getP2().getX() + 1))
        y_range = range(int(self.shape.getP1().getY()), int(self.shape.getP2().getY() + 1))
        return (round(point.getX()) in x_range) and (round(point.getY()) in y_range)

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
