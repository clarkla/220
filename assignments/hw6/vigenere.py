from graphics import *


win = GraphWin("Vigenere", 600, 400)


def gui():      # Creates window and entry boxes

    # Create message entry box and instructions
    message_instructions = Text(Point(100, 80), "Enter Message to Encode:")
    message_instructions.setSize(12)
    message_instructions.draw(win)
    message_entry = Entry(Point(340, 80), 30)
    message_entry.draw(win)

    # Create keyword entry box and instructions
    key_instructions = Text(Point(138, 120), "Enter Keyword:")
    key_instructions.setSize(12)
    key_instructions.draw(win)
    key_entry = Entry(Point(340, 120), 30)
    key_entry.draw(win)

    win.getMouse()

    # Assign entries to variables and return those values
    message = message_entry.getText()
    key = key_entry.getText()

    return message, key


def code():     # Encode message
    # Define alphabet list for later indexing, assign previous returned values, create empty list
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    message, key = gui()
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

    # Join appended new letters together and print them
    encoded_message = "".join(encoded_list)
    print(encoded_message)


def main():
    gui()
    code()


if __name__ == "__main__":
    main()
