"""
Name: Luke Clark
vigenere.py

Problem: This program implements a vigenere cipher into a graphical interface

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def code(message, key):     # Encode message
    # Define alphabet list for later indexing, create empty list
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    encoded_list = []

    # Parse message to remove spaces and switch to upper case
    message_uppercase = message.upper()
    message_final = message_uppercase.replace(" ", "")

    # Parse key to remove spaces and switch to upper case
    key_uppercase = key.upper()
    key_no_space = key_uppercase.replace(" ", "")

    # Make key repeat, cut off at length of message (ie. ABC to ABCABCABC)
    key_temp = key_no_space * len(message_final)
    key_final = key_temp[0:len(message_final)]

    # Using index of alphabet list, add together numbers of index from both message and key
    # If index exceeds 25, subtract 26 to put it back in alphabet index range
    # Append new letter to previous empty list
    for i in range(len(message_final)):
        new_index = alphabet.index(message_final[i]) + alphabet.index(key_final[i])
        if new_index > 25:
            new_index -= 26
        new_letter = alphabet[new_index]
        encoded_list.append(new_letter)

    # Join appended new letters together for later printing
    encoded_message = "".join(encoded_list)
    return encoded_message


def main():
    win = GraphWin("Vigenere", 600, 400)

    # Create message and key entry boxes and instructions
    message_instructions = Text(Point(100, 80), "Enter Message to Encode:")
    message_instructions.setSize(12)
    message_instructions.draw(win)
    message_entry = Entry(Point(340, 80), 30)

    key_instructions = Text(Point(138, 120), "Enter Keyword:")
    key_instructions.setSize(12)
    key_instructions.draw(win)
    key_entry = Entry(Point(340, 120), 30)
    key_entry.draw(win)
    message_entry.draw(win)

    # Create encode button
    encode_instructions = Text(Point(300, 200), "Encode")
    encode_instructions.setSize(12)
    encode_instructions.draw(win)
    rectangle1 = Rectangle(Point(230, 170), Point(370, 230))
    rectangle1.draw(win)

    # Wait for button click
    win.getMouse()

    # Assign entries to variables and run code function using them
    message = message_entry.getText()
    key = key_entry.getText()
    encoded_message = code(message, key)

    # Un-draw encode button and print newly encoded message
    encode_instructions.undraw()
    rectangle1.undraw()
    resulting_message = Text(Point(300, 250), "Resulting Message")
    resulting_message.setSize(12)
    resulting_message.draw(win)
    final_message = Text(Point(300, 270), encoded_message)
    final_message.setSize(12)
    final_message.draw(win)

    # Wait for final click and close the program
    final_instructions = Text(Point(300, 380), "Click anywhere to close window")
    final_instructions.draw(win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
