"""
Name: Thomas Scola
hw2.py

Problem: To implement loops and calculations in our code

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def sum_of_threes():
    sum_total = 0
    upper_bound = eval(input("what is the upper bound? "))
    for i in range(0, upper_bound + 1, 3):
        sum_total = sum_total + i
    print("sum of threes is", sum_total)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()


def triangle_area():
    length_a = eval(input("Enter the length of side a: "))
    length_b = eval(input("Enter the length of side b: "))
    length_c = eval(input("Enter the length of side c: "))
    side = (length_a + length_b + length_c) / 2
    area_squared = side * (side - length_a) * (side - length_b) * (side - length_c)
    area = math.sqrt(area_squared)
    print("The area is: ", area)

def sum_squares():
    square_sum = 0
    lower_range = eval(input("Enter the lower range: "))
    upper_range = eval(input("Enter the upper range: "))
    for i in range(lower_range, upper_range + 1):
        square_sum = square_sum + (i*i)
    print(square_sum)


def power():
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    product = 1
    for i in range(exponent):
        product = product * base

    print(exponent, "^",base, "=",product)


if __name__ == '__main__':
    pass
