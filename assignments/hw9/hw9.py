"""
Name: Thomas Scola
hw9.py
Problem: Create a function that uses boolean functions and GUI's to simulate a game of hangman
Certification of Authenticity:
I received help from the CSL with Brooke Duvall.
"""
import random
from graphics import*


def get_words(file_name): #allows the user to input their document namem
    infile = open(file_name, 'r')
    words = infile.readlines()
    return words


def get_random_word(words):
    random_int = random.randint(0, len(words) - 1)
    word = words[random_int]
    return word[:-1]


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    return False


def make_hidden_secret(secret_word, guesses): # progess for hidden word
    blank = [] * len(secret_word)
    for i in range(len(secret_word)):
        blank.append('_ ')
    secret_word_list = []   #alist for the correct guesses
    secret_word_list[:] = secret_word
    for i in range(len(secret_word)): #a list for the correct guesses
        for j in range(len(guesses)):
            if guesses[j] == secret_word_list[i]:
                blank[i] = guesses[j] + " "
    return "".join(blank).strip()


def won(guessed):
    for i in guessed:
        if i == '_':
            return False
    return True

def play_graphics(secret_word):
    #graphics for the window
    win = GraphWin("Secret Door", 1000, 1000)
    win.setBackground('white')

    #the graphics for the hang post and rope
    arm_of_post = Line(Point(300, 100), Point(550, 100))
    arm_of_post.draw(win)
    post = Line(Point(550, 100), Point(550, 750))
    post.draw(win)
    base_of_post = Line(Point(150, 600), Point(700, 750))
    base_of_post.draw(win)
    rope = Line(Point(300, 200), Point(300, 350))
    rope.draw(win)

    #the graphics for the body
    head = Circle((400, 350), 100)
    head.draw(win)
    torso = Line(Point(400, 220), Point(400, 440))
    torso.draw(win)
    #right_arm = Line(Point(400))

    #I worked on the grpahic a bit but i could not get the play command to work.



    pass


def play_command_line(secret_word):
    guessed = []
    guess = ''
    num = 6
    print(won(make_hidden_secret(secret_word, guessed)))
    while num > 0 and not won(make_hidden_secret(secret_word, guessed)):
        valid_guess = False
        while not valid_guess:
            print("already guessed: " + str(guessed))
            print("guess remaining: ", num)
            print(make_hidden_secret(secret_word, guessed))
            guess = input('guess a letter: ')
            if not already_guessed(guess, guessed):
                valid_guess = True
        guessed.append(guess)
        if not letter_in_secret_word(guess,secret_word):
            num = num - 1
    if won(make_hidden_secret(secret_word, guessed)):
        print("You won!")
    else:
        print("You lose!")









if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
