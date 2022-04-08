"""
Name: Thomas Scola
lab11.py
Problem: to form a proggram that imports lab10.door door and button
Certification of Authenticity:
I certify this is completely my work
"""
from lab10.door import Door
from lab10.button import Button
from graphics import*
from random import randint
def three_door_game():
    win = GraphWin("Secret Door", 800, 600)
    win.setBackground('purple')
    text_box = Text(Point(400, 150), "Pick a door")
    text_box.draw(win)
    quit_box = Button(Rectangle(Point(600, 50), Point(700, 100)), "Quit")
    quit_box.draw(win)
    door_object_1 = Door(Rectangle(Point(100, 350), Point(200, 500)), "Door 1")
    door_object_1.color_door('cyan')
    door_object_1.draw(win)
    door_object_2 = Door(Rectangle(Point(250, 350), Point(350, 500)), "Door 2")
    door_object_2.color_door('cyan')
    door_object_2.draw(win)
    door_object_3 = Door(Rectangle(Point(400, 350), Point(500, 500)), "Door 3")
    door_object_3.color_door('cyan')
    door_object_3.draw(win)

    point = win.getMouse()
    while not quit_box.is_clicked(point):
        if door_object_1.is_clicked(point):
            if door_object_1.is_secret():
                door_object_1.undraw()
                door_object_1.open("white", "open")
                door_object_1.draw(win)
            else:
                door_object_1.undraw()
                door_object_1.close("cyan", "close")
                door_object_1.draw(win)
        if door_object_2.is_clicked(point):
            if door_object_2.is_secret():
                door_object_2.undraw()
                door_object_2.open("white", "open")
                door_object_2.draw(win)
            else:
                door_object_1.undraw()
                door_object_1.close("cyan", "close")
                door_object_1.draw(win)
        if door_object_3.is_clicked(point):
            if door_object_3.is_secret():
                door_object_1.undraw()
                door_object_1.open("white", "open")
                door_object_1.draw(win)
            else:
                door_object_1.undraw()
                door_object_1.close("cyan", "close")
                door_object_1.draw(win)
        point = win.getMouse()