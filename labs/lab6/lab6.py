"""
Name: Luke Clark
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter first name and last name: ")
    name_list = name.split(" ")
    print(name_list[1] + ", " + name_list[0])


def company_name():
    company = input("Enter company domain name: ")
    company_list = company.split(".")
    print(company_list[1])


def initials():
    total = eval(input("How many names will be input? "))
    for i in range(1, total + 1):
        first_name = input("Enter the first name of student " + str(i) + ": ")
        last_name = input("Enter " + first_name + "'s last name: ")
        print(first_name + "'s initials are " + first_name[0] + last_name[0])


def names():
    names_list = input("Enter names separated by commas: ")
    names_split = names_list.split(", ")
    print("The initials are", end=" ")
    for i in names_split:
        name_split = i.split(" ")
        initials = name_split[0][0] + name_split[1][0]
        print(initials, end=" ")


def thirds():
    total = eval(input("Enter number of sentences: "))
    for _ in range(total):
        sentence = input("Enter sentence: ")
        for i in sentence[2::3]:
            print(i, end="")
        print()


def word_average():
    sentence = input("Enter sentence: ")
    words_list = sentence.split(" ")
    acc = 0
    for i in words_list:
        acc += len(i)
    average = acc / len(words_list)
    print(average)


def pig_latin():
    sentence = input("Enter sentence: ")
    sentence_lower = sentence.lower()
    words_list = sentence_lower.split(" ")
    for i in words_list:
        print(i[1:] + i[0] + "ay", end=" ")


def main():
    name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()


main()
