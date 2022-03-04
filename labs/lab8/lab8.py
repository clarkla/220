"""
Name: Luke Clark
lab8.py
"""

from function import encode


def number_words(in_file_name, out_file_name):
    file1 = open(in_file_name, "r")
    file2 = open(out_file_name, "w")
    acc = 1
    for i in file1:
        words = i.split()
        for x in range(0, len(words)):
            print(str(acc) + " " + words[x], file=file2)
            acc += 1


def hourly_wages(in_file_name, out_file_name):
    file1 = open(in_file_name, "r")
    file2 = open(out_file_name, "w")
    for i in file1:
        words = i.split()
        new_wage = int(words[2]) + 1.65
        weekly_pay = new_wage * int(words[3])
        print(str(words[0]) + " " + str(words[1]) + " " + str(round(weekly_pay, 2)), file=file2)


def calc_check_sum(isbn) -> int:
    acc1 = 0
    acc2 = 10
    for i in isbn:
        acc1 += int(i) * acc2
        acc2 -= 1
    return acc1


def send_message(file, friend):
    file1 = open(file, "r")
    file2 = open(str(friend) + ".txt", "w")
    for i in file1:
        print(i, file=file2, end="")


"""
def encode(message, key):
    encoded = []
    for i in message:
        shift = ord(i) + key
        encoded.append(chr(shift))
    return "".join(encoded)
"""


def send_safe_message(file, friend, key):
    file1 = open(file, "r")
    file2 = open(str(friend) + ".txt", "w")
    for i in file1:
        words = i.split()
        for x in range(len(words)):
            print(encode(words[x], key), file=file2)


def encode_better(message, key):
    encoded = []
    for i in range(len(message)):
        shift = (ord(message[i]) + ord(key[i]) - 97)
        encoded.append(chr(shift))
    return "".join(encoded)


def send_uncrackable_message(file, friend, pad):
    file1 = open(file, "r")
    file2 = open(str(friend) + ".txt", "w")
    file3 = open(pad, "r")
    for i in file1:
        words = i.split()
        for x in range(len(words)):
            print(encode_better(words[x], file3), file=file2)


def main():
    # number_words("walrus.txt", "walrus_output.txt")
    # hourly_wages("hourly_wages.txt", "hourly_output.txt")
    # print(calc_check_sum("0072946520"))
    # send_message("message.txt", "bob")
    # send_safe_message("message.txt", "bob", 3)
    send_uncrackable_message("message.txt", "bob", "pad.txt")
    pass


main()
