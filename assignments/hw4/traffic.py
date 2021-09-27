"""
Name: Luke Clark
traffic.py

Problem: This programs calculates average number of cars travelling on
a certain amount of roads over a certain number of days.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    roads = eval(input("How many roads were surveyed? "))
    cars = 0
    acc = 0
    for i in range(1, roads + 1):
        acc = 0
        days = eval(input("How many days was road " + str(i) + " surveyed? "))
        for day in range(1, days + 1):
            acc += eval(input("How many cars traveled on day " + str(day) + "? "))
        cars += acc
        avg_day = acc / days
        print("Road " + str(i) + " average vehicles per day: " + str(round(avg_day, 2)))
    avg_total = cars / roads
    print("Total number of vehicles traveled on all roads: " + str(cars))
    print("Average number of vehicles per road: " + str(round(avg_total, 2)))


if __name__ == "__main__":
    main()
