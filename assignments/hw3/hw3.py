"""
Name: Thomas Scola
hw3.py

Problem: to perform calculations using loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    num_grades = eval(input("How many grades will you enter? "))
    acc = 0
    for i in range(num_grades):
        grade = eval(input("Enter grade: "))
        acc = acc + grade

    calculations = acc / num_grades
    print("average is: ", calculations)


def tip_jar():
    acc = 0
    for i in range(5):
        donation = eval(input("Enter donation amount: "))
        acc = acc + donation

    print("total tips", acc)


def newton():
    num_value = eval(input("Enter the x value."))
    approx = num_value
    improvement_amount = eval(input("How many times to improve approximations? "))
    for i in range(improvement_amount):
        approx = (approx + (num_value / approx)) / 2
    print("The square root is approximately: ", approx)


def sequence():
    n_terms = eval(input("Enter the number of terms for the sequence: "))
    for i in range(1, n_terms + 1):
        print((i-1) + (i % 2), end=" ")



def pi():
    n_terms = eval(input("Enter the number of terms for the series: "))
    acc = 1
    for i in range(n_terms):
        numer = i + (2 - (i % 2))
        denom = i + (1 + (i % 2))
        acc *= numer / denom
    product = acc * 2
    print(product)


if __name__ == '__main__':
    pass
