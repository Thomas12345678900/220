"""
Name: Thomas Scola
hw6.py

Problem: To create programs that utilize floats, encoding, and the return function

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    cash = float(input("Enter an integer: "))
    print("That is ${:.2f}".format(cash))


def encode():
    message_to_code = input("Enter a message")
    key = eval(input("Enter a key: "))
    string_collector = ""
    for i in range(len(message_to_code)):
        ordinal = ord(message_to_code[i])
        total = key + ordinal
        char = chr(total)
        string_collector = string_collector + char
    print(string_collector)

def sphere_area(radius):
    area_sphere = 4 * (math.pi) * (radius**2)
    return area_sphere


def sphere_volume(radius):
    volume_sphere = 4/3 * (math.pi) * (radius**3)
    return volume_sphere


def sum_n(number):
    sum = number * ((number + 1)/2)
    return sum


def sum_n_cubes(number):
    num_cubes = (number * (number + 1)/2) **2
    return num_cubes


def encode_better():
    message_to_code = input('Enter your message to be coded: ')
    key_word = input("enter the keyword")
    total = ""
    for i in range(len(message_to_code)):
        message = ord(message_to_code[i]) - 65
        key = ord(key_word[i % len(key_word)]) - 65
        encoded_message = message + key
        encoded_message = encoded_message % 58
        final_answer = encoded_message + 65
        finall_answer = chr(final_answer)
        total = total + finall_answer

    print(total)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
