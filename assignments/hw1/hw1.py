"""
Name: Thomas Scola
GettingStarted.py

Problem: to form a program that does inputs and calculations

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area = ", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Area = ", volume)


def shooting_percentage():
    total_shot = eval(input("Enter the player's total shots: "))
    made_shot = eval(input("Enter the player's shots made: "))
    shots_made_percentage = ((made_shot)/(total_shot)) * 100
    print("The player's shooting percentage is ", shots_made_percentage)


def coffee():
    pounds = eval(input("Enter how many pounds of coffee to be purchased: "))
    price = (10.50 * pounds) + (0.86 * pounds) + 1.50
    print("Your total costs are: ", price)


def kilometers_to_miles():
    kilometers = eval(input("how many kilometers did you travel? "))
    miles = kilometers / 1.61
    print("That is",miles, "miles!")

if __name__ == '__main__':
    pass
