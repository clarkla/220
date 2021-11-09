"""
Name: Luke Clark
three_door_game.py

Problem: This program simulates a random three door game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import choice
from graphics import Rectangle, GraphWin, Point, Text
from button import Button


# Function to identify which door was clicked
def chosen_door(click, door1, door2, door3):
    door = ""
    if door1.is_clicked(click) is True:
        door = door1
    elif door2.is_clicked(click) is True:
        door = door2
    elif door3.is_clicked(click) is True:
        door = door3
    return door


def main():
    # Create window, instructions, and shapes for the doors
    win = GraphWin("Door Game", 400, 400)

    inst = Text(Point(200, 50), "Choose the right door")
    inst.draw(win)

    button1 = Rectangle(Point(70, 120), Point(140, 270))
    button2 = Rectangle(Point(170, 120), Point(240, 270))
    button3 = Rectangle(Point(270, 120), Point(340, 270))

    # Create Button objects to represent doors using previous shapes
    door1 = Button(button1, "1")
    door1.draw(win)
    door2 = Button(button2, "2")
    door2.draw(win)
    door3 = Button(button3, "3")
    door3.draw(win)

    # Determine which door from the list is the winning door and initialize further text
    doors = [door1, door2, door3]
    door_winner = choice(doors)
    winner_inst = Text(Point(200, 50), "you win!")
    loser_inst = Text(Point(200, 50), "you lost! :(")
    door_inst = Text(Point(200, 360), "door{} was the correct door".format(door_winner.get_label()))
    close_inst = Text(Point(200, 380), "click to close")

    # Loop click until user has clicked a door
    click = win.getMouse()
    while (door1.is_clicked(click) or door2.is_clicked(click) or door3.is_clicked(click)) is False:
        click = win.getMouse()

    # If the door that was clicked is the winning door, color door green and draw winning text
    if chosen_door(click, door1, door2, door3) == door_winner:
        chosen_door(click, door1, door2, door3).color_button("green")
        inst.undraw()
        winner_inst.draw(win)
        close_inst.draw(win)
    # If the door was not the winning door, color it red and draw losing text
    else:
        chosen_door(click, door1, door2, door3).color_button("red")
        inst.undraw()
        loser_inst.draw(win)
        door_inst.draw(win)
        close_inst.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
