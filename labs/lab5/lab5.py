"""
Name: Thomas Scola
lab5.py
Problem: to form a program that calculates a greeting card
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import*
from math import*

def triangle():
    win = GraphWin("Triangle", 600, 600)

    instructions = Text(Point(300, 500), "Click three times to draw a triangle")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    p1_x = p1.getX()
    p1_y = p1.getY()
    p2_x = p2.getX()
    p2_y = p2.getY()
    p3_x = p3.getX()
    p3_y = p3.getY()

    side_1_x = p2_x - p1_x
    side_1_y = p2_y - p1_y
    side_2_x = p2_x - p3_x
    side_2_y = p2_y - p3_y
    side_3_x = p3_x - p1_x
    side_3_y = p3_y - p1_y
    side_1_length = sqrt((side_1_x ** 2) + (side_1_y ** 2))
    side_2_length = sqrt((side_2_x ** 2) + (side_2_y ** 2))
    side_3_length = sqrt((side_3_x ** 2) + (side_3_y ** 2))

    perimeter = side_1_length + side_2_length + side_3_length
    all_sides = perimeter / 2
    area = sqrt(all_sides * ((all_sides - side_1_length) * (all_sides - side_2_length) * (all_sides - side_3_length)))

    user_triangle = Polygon(p1, p2, p3)
    user_triangle.setFill("light blue")
    area_display = Text(Point(300, 400), " ")
    perimeter_display = Text(Point(300, 450), " ")
    area_output = "Area:", area
    perimeter_output = "Perimeter:", perimeter
    area_display.setText(area_output)
    perimeter_display.setText(perimeter_output)

    user_triangle.draw(win)
    area_display.draw(win)
    perimeter_display.draw(win)

    instructions.setText("Click to close")
    win.getMouse()
    win.close()

def color_shape():
    """Create code to allow a user to color a shape by entering rgb amounts"""

    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    message = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), message)
    inst.draw(win)

    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    width = 5
    red_box = Entry(Point(win_width / 2, 240), width)
    green_box = Entry(Point(200, 270), width)
    blue_box = Entry(Point(200, 300), width)

    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for colors in range(5):

        win.getMouse()
        red_val = red_box.getText()
        green_val = green_box.getText()
        blue_val = blue_box.getText()

        int_red_val = int(red_val)
        int_green_val = int(green_val)
        int_blue_val = int(blue_val)

        shape.setFill(color_rgb(int_red_val, int_green_val, int_blue_val))

    click_close = "Click to Close"
    inst.setText(click_close)
    win.getMouse()
    win.close()

def process_string():
    stringg = input("Enter a string ")
    first_letter = stringg[0]
    last_letter = stringg[-1]
    two_five = stringg[2:5+1]
    concat = first_letter + last_letter
    first_three = stringg[0:2] * 10
    lens_x = len(stringg)
    print(first_letter)
    print(last_letter)
    print(two_five)
    print(concat)
    print(first_three)
    print(lens_x)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, 7.2]
    hi_there = values[1] + values[3]
    result = values[0] + values[2]
    hi_ten = values[1] *10
    list_1 = [values[2], values[3], values[4]]
    list_2 = [values[2], values[3], values[1]]
    list_3 = [values[0], values[2], values[5]]
    result_2 = values[0] + values[2] + values[5]
    print(hi_there)
    print(result)
    print(hi_ten)
    print(list_1)
    print(list_2)
    print(list_3)
    print(result_2)
    # str() int() float()
process_list()

def another_series():
    n_terms = eval(input("How many terms would you like to do: "))
    for i in range(n_terms):
        print(17%3, end=" ")
        print(34%6, end=" ")
        print(78%72, end=" ")



def target():
    # creates the window
    win_length = 250
    win = GraphWin("Target", win_length, win_length)
    mid_point = Point(win_length / 2, win_length / 2)

    yellow_rad = 50 / 2

    white_circle = Circle(mid_point, yellow_rad * 5)
    black_circle = Circle(mid_point, yellow_rad * 4)
    blue_circle = Circle(mid_point, yellow_rad * 3)
    red_circle = Circle(mid_point, yellow_rad * 2)
    yellow_circle = Circle(mid_point, yellow_rad)

    white_circle.setFill("white")
    black_circle.setFill("black")
    blue_circle.setFill("blue")
    red_circle.setFill("red")
    yellow_circle.setFill("yellow")

    white_circle.draw(win)
    black_circle.draw(win)
    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_circle.draw(win)

    closing = Text(mid_point, "Click to close")
    closing.draw(win)
    win.getMouse()
    win.close()
