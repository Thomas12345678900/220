"""
Name: Thomas Scola
lab6.py
Problem: create a vigenere cipher using a GUI
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import*

def vigenere():
    win = GraphWin("Vigenere Cipher", 600, 600)

    win.setCoords(0.0, 0.0, 3.0, 4.0)
    Text(Point(1, 3), " Celsius temperature:").draw(win)
    Text(Point(1, 1), "Hahrenekheir: ").draw(win)
    input_text = Entry(Point(2.25, 3), 5)
    input_text.setText(" ")
    input_text.draw(win)
    output_text = Text(Point(2.25, 1), "")
    output_text.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
    win.getMouse()
    output_text.setText()
    button.setText("Quit")
    win.getMouse()

    total = ""
    message_to_code = input('Enter your message to be coded: ')
    key_word = input("enter the keyword")
    message_to_code = message_to_code.upper()
    message_to_code = message_to_code.replace("", "")
    key_word = key_word.upper()
    key_word = key_word.replace("", "")

    for i in range(len(message_to_code)):
        message = ord(message_to_code[i]) - 65
        key = ord(key_word[i%len(key_word)]) -65
        encoded_message = message + key
        encoded_message = encoded_message % 26
        final_answer = encoded_message + 65
        finall_answer = chr(final_answer)
        total = total + finall_answer

    print(total)
