"""
Name: Thomas Scola
lab2.py
Problem: to form a program that calculates monthly interest
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def means():
    num_values = eval(input("How many values will be entered: ")) #enters the number of values
    avg = 0 #accumulator for regular average
    root = 0 #accumulator for root mean square
    harmonic = 0 #accumulator for harmonic mean
    geo = 1 #accumulator for geometric mean

    #for loop that performs the summations for entered values
    for i in range(num_values):
        values = eval(input("Enter your values: ")) #enter values
        avg = avg + values
        root = root + values ** 2
        harmonic = harmonic + (values ** -1)
        geo = geo * values

    #calculations
    average = avg / num_values
    root_mean_square = math.sqrt(root / num_values)
    harmonic_mean = (num_values) / (harmonic)
    geometric_mean = (geo) ** (1 / num_values)

    #outputs
    print("The output for average is: ", average)
    print("The putput for the root-mean-square is: ", root_mean_square)
    print("The output for the harmonic mean is: ", harmonic_mean)
    print("The output for the geometric mean is: ", geometric_mean)

means()