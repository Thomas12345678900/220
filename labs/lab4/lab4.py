"""
Name: Thomas Scola
lab3.py
Problem: to form a program that calculates a greeting card
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import time

from graphics import GraphWin, Circle, Text, Polygon, Point, Line

def greeting_card():
    win = GraphWin("Happy Valentine's Day!", 500, 500)
    win.setBackground("pink")
    message = Text(Point(100, 25), "Happy Valentine's Day!")
    message.draw(win)
    end_message = Text(Point(250, 400), "")
    end_message.draw(win)
    circle = Circle(Point(170, 150), 87.25)
    circle.setFill("red")
    circle.setOutline('red')
    circle.draw(win)

    circle_2 = Circle(Point(330, 150), 87.25)
    circle_2.setFill("red")
    circle_2.setOutline("red")
    circle_2.draw(win)

    tri_angle = Polygon(Point(85, 175), Point(415, 175), Point(250, 400))
    tri_angle.draw(win)
    tri_angle.setFill("red")
    tri_angle.setOutline("red")

    a_line = Line(Point(5, 0), Point(220, 150))
    a_line.draw(win)
    a_line.setArrow("last")
    for i in range(30):
        a_line.move(20, 18)
        time.sleep(0.1)
    end_message.setText("Click anywhere to close the program.")
    win.getMouse()


    win.close()

greeting_card()