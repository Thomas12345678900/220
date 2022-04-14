"""
Name: Thomas Scola
lab12.py
Problem: to form a program that works with while loops and other liste methods
Certification of Authenticity:
I received help from the CSL lab with Brooke Duvall
"""

from random import randint
def find_and_remove_first(list, value):
    i = 0
    while i < len(list):

        if list[i] == value:
            list.pop(i)
            list.insert(list[i], 'Thomas')
        i = i + 1


def good_input():
    input_num = eval(input("Enter your value"))

    while 1 >= input_num <= 10:
        if input_num > 10:
            print("no that is too big")
            input_num = eval(input("Enter your value"))
        elif input_num < 1:
            print("no that is too small")
            input_num = eval(input("Enter your value"))
    print('That is a good value')
    return input_num



def num_digits():
    input_number = eval(input("Enter your number"))

    while input_number > 0:
        counter = 0
        while input_number > 0:
            counter += 1
            input_number = input_number //10
        print(counter)

        input_number = eval(input("Enter your number"))

def hi_lo_game():
    number = randint(1, 100)
    guess = 0
    num_guesses = 0
    while guess != number and num_guesses < 7:
        guess = int(input("Guess the Number : "))
        num_guesses += 1
        if guess == number:
            print("You guessed the right number!")
        elif guess > number:
            print("You guessed too high!")
        elif guess < number:
            print("You guessed too low!")
    if guess == number:
        print("you won in " +str(num_guesses)+ " guesses")
    else:
        print("The number was ", number)