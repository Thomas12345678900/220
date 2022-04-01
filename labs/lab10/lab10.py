"""
Name: Thomas Scola
lab10.py
Problem: to form a program that combines door.py and button.py
Certification of Authenticity:
I had the assistance of brooke duvall from the CSL
"""
from graphics import *
from button import Button
from door import Door


def main():
    win = GraphWin("Secret Door", 500, 500)
    win.setBackground('purple')

    door_object = Door(Rectangle(Point(200, 250), Point(300, 400)), "close")
    door_object.color_door('cyan')
    door_object.draw(win)
    button_object = Button(Rectangle(Point(200, 60), Point(250, 100)), "button")
    button_object.color_button('black')
    button_object.draw(win)

    point = win.getMouse()
    while not button_object.is_clicked(point):
        if door_object.is_clicked(point):
            if door_object.get_label() == "open":
                door_object.undraw()
                door_object.open("white", "open")
                door_object.draw(win)
            elif door_object.get_label() == "close":
                door_object.undraw()
                door_object.close("cyan", "close")
                door_object.draw(win)
        point = win.getMouse()
