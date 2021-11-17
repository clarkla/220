"""
Name: LUKE CLARK
lab12.py
"""
from random import randint


def find_and_remove_first(list, value):
    list.insert(list.index(value), "Luke")
    list.remove(value)


def read_data(filename):
    list = []
    file = open(filename, "r")
    line = file.readline()
    while line != '':
        split_line = line.split()
        count = 0
        while count < len(split_line):
            list.append(int(split_line[count]))
            count += 1
        line = file.readline()
    return list


def is_in_linear(search_val, values):
    count = 0
    while count < len(values):
        if search_val == values[count]:
            return True
        count += 1
    return False


def good_input():
    value = int(input("Enter number between 1-10: "))
    while not 1 <= value <= 10:
        value = int(input("Number not between 1 and 10. Enter another: "))
    return value


def num_digits():
    value = 1
    while value >= 1:
        value = int(input("Enter positive number: "))
        count = 0
        temp = value
        if temp >= 1:
            while temp != 0:
                temp //= 10
                count += 1
            print(count)


def hi_lo_game():
    correct = randint(1, 100)
    count = 0
    guess = 0
    while count < 7 and guess != correct:
        guess = int(input("Enter guess: "))
        if guess > correct:
            print("Too high")
        if guess < correct:
            print("Too low")
        if guess == correct:
            print("Correct")
        count += 1
    if guess == correct:
        print("Wow! You won in {} guesses!".format(count))
    else:
        print("you lost. the number was {}".format(correct))


def main():
    # find_and_remove_first([1, 2, 3], 2)
    # print(read_data("dataSorted.txt"))
    # print(is_in_linear(265, read_data("dataSorted.txt")))
    # print(good_input())
    # num_digits()
    hi_lo_game()


main()
