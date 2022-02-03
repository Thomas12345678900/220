"""
Name: Thomas Scola
lab3.py
Problem: to form a program that calculates average cars on the road
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def traffic():
    num_roads = eval(input("Enter the number of roads: "))
    acc_two = 0 #used for accumulating for total number of cars
    for i in range(num_roads):
        print("Enter the number of days for road ", i+1)
        num_days = eval(input(" "))
        acc = 0 #used for accumualating the cars under number of days
        for j in range(num_days):
            print("\tEnter the number of cars for day ", j+1)
            num_cars = eval(input("\t "))
            acc = acc + num_cars
            acc_two = acc_two + num_cars
        average = acc / num_days
        print("The average for road ", i+1 , "is", average)

    average_2 = acc_two / num_roads
    print("The total number of cars traveled on all roads: ", acc_two)
    print("The average number of vehicles per road: ", average_2)

traffic()
