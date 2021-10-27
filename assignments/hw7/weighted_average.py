"""
Name: Luke Clark
weighted_average.py

Problem: This program calculates student's grades from an input file and writes
them to an output file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    # Open files for input and output
    file1 = open(in_file_name, "r")
    file2 = open(out_file_name, "w")

    # Define an empty list for later class average calculation
    average_list = []

    # Repeat code for each line in the file
    for i in file1:
        # Split list into student name and numbers of grades/weights
        list1 = i.split(":")
        name = list1[0]
        number_list = list1[1].split()

        # Define new lists for weights and grades separately and converted into integers
        weight_list = []
        grade_list = []
        for weight in number_list[::2]:
            weight_list.append(int(weight))
        for grade in number_list[1::2]:
            grade_list.append(int(grade))

        # If sum of weights is 100, calculate average
        if sum(weight_list) == 100:
            average = 0

            # Iterate through both lists and calculate average
            for x in range(len(weight_list)):
                average += (weight_list[x] * grade_list[x])
            average /= 100

            # Append calculated average to empty list for class average calculation
            average_list.append(average)

            # Write output to file
            print(name + "'s average: " + str(round(average, 1)), file=file2)

        # If weight is greater than or less than 100, print error message to file
        elif sum(weight_list) > 100:
            print(name + "'s average: Error: The weights are more than 100.", file=file2)
        elif sum(weight_list) < 100:
            print(name + "'s average: Error: The weights are less than 100.", file=file2)

    # Print the total class average  (This was what produced the pytest index error. I originally
    #   printed a new line before "class average," which caused all tests to fail)
    print("Class average: " + str(round(sum(average_list) / len(average_list), 1)), file=file2)

    file1.close()
    file2.close()


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
