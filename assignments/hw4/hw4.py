"""
Name: Thomas Scola
hw4.py

Problem: Use graphics to solve the homework

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from math import sqrt, pi
from graphics import Point, GraphWin, Circle, Text, Rectangle


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("square", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(100, 100), Point(150, 150))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        new_shape = shape.clone()
        shape.move(change_x, change_y)
        new_shape.draw(win)
    instructions.undraw()
    closing_message = Text(inst_pt, "Click to close")
    closing_message.draw(win) 
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 500, 500)
    win.setCoords(0, 0, 10, 10)

    message = Text(Point(5,1), "Click twice to draw a new rectangle")
    message.draw(win)

    point_one = win.getMouse()
    point_one.draw(win)
    point_two = win.getMouse()
    point_two.draw(win)
    pone_x = point_one.getX()
    ptwo_x = point_two.getX()
    pone_y = point_one.getY()
    ptwo_y = point_two.getY()

    rectangle_made = Rectangle(Point(pone_x, pone_y), Point(ptwo_x, ptwo_y))
    rectangle_made.setFill("green")
    rectangle_made.draw(win)

    perimeter_textbox = Text(Point(5, 3), "Perimeter: ")
    area_textbox = Text(Point(5, 2.5), "Area: ")
    perimeter_textbox.draw(win)
    area_textbox.draw(win)

    length = abs(point_two.getY() - point_one.getY())
    width = abs(point_two.getX() - point_one.getY())
    area = length * width
    perimeter = 2 * area

    perimeter_value = Text(Point(6.5, 3), perimeter.__round__(3))
    area_value = Text(Point(6, 2.5), area.__round__(3))
    perimeter_value.draw(win)
    area_value.draw(win)

    message.setText("Click to close")
    win.getMouse()
    win.close()

def circle():
    win = GraphWin("Double Click circle", 600, 600)

    center = win.getMouse()
    point = win.getMouse()

    dX = point.getX() - center.getX()
    dY = point.getY() - center.getY()

    radius = sqrt(dX **2 + dY **2)
    circle = Circle(center, radius)

    circle.setFill("light blue")
    circle.draw(win)

    radius_text_box = Text(Point(300, 550), "Radius: ")
    radius_text_box.draw(win)

    radius_value = Text(Point(350, 550), radius.__round__(3))
    radius_value.draw(win)

    win.getMouse()
    win.close()


def pi2():
    summing_terms = eval(input("Enter the number of terms to sum: "))
    pi_approx = 0
    denom = 1
    sign_of_term = 1

    for i in range(summing_terms):
        pi_approx = pi_approx + (sign_of_term * (4 / denom))
        denom = denom + 2
        sign_of_term = sign_of_term * -1

    accuracy = abs(pi - pi_approx)

    print("The pi approximation ", pi_approx)
    print("The accuracy is ", accuracy)


if __name__ == '__main__':
    pass
