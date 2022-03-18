"""
Name: Thomas Scola
lab8.py
Problem: create a program that simulates bumper cars that bump into each other using graphics
Certification of Authenticity:
I worked on this assignment with Ethan Kidwell. All rights go to us.
"""
import time
from random import randint
from math import sqrt
from graphics import *


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(circle_ball, circle_ball_2):
    circle_1_radius = circle_ball.getRadius()
    circle_2_radius = circle_ball_2.getRadius()
    circles_radius = circle_1_radius + circle_2_radius
    circle_1_center = circle_ball.getCenter()
    circle_2_center = circle_ball_2.getCenter()
    circle_1_x = circle_1_center.getX()
    circle_1_y = circle_1_center.getY()
    circle_2_x = circle_2_center.getX()
    circle_2_y = circle_2_center.getY()
    circle_distance = sqrt(((circle_2_x - circle_1_x) ** 2)+((circle_2_y - circle_1_y) ** 2))
    if circle_distance <= circles_radius:
        return True
    else:
        return False


def hit_vertical(circle_ball, graphwin):
    circle_radius = circle_ball.getRadius()
    window_height = graphwin.getHeight()
    circle_center = circle_ball.getCenter()
    circle_y = circle_center.getY()
    if circle_y == (window_height - circle_radius):
        return True
    elif circle_y == circle_radius:
        return True
    else:
        return False


def hit_horizontal(circle_ball, graphwin):
    circle_radius = circle_ball.getRadius()
    win_width = graphwin.getWidth()
    circle_center = circle_ball.getCenter()
    circle_x = circle_center.getX()
    if circle_x == (win_width - circle_radius):
        return True
    elif circle_x == circle_radius:
        return True
    else:
        return False


def get_random_color():
    rgb1 = randint(0, 255)
    rgb2 = randint(0, 255)
    rgb3 = randint(0, 255)
    randomm_color = color_rgb(rgb1, rgb2, rgb3)
    return randomm_color


def bumper():
    window = GraphWin("Bumper Cars Simulation", 1000, 600)
    window_height = window.getHeight()
    window_width = window.getWidth()

    randomm_radius_1 = randint(10, 100)
    randomm_x_1 = randint(randomm_radius_1, window_width)
    randomm_y_1 = randint(randomm_radius_1, window_height)
    randomm_x_2 = randint(randomm_radius_1, window_width)
    randomm_y_2 = randint(randomm_radius_1, window_height)

    circle_1 = Circle(Point(randomm_x_1, randomm_y_1), randomm_radius_1)
    circle_2 = Circle(Point(randomm_x_2, randomm_y_2), randomm_radius_1)

    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())

    circle_1.draw(window)
    circle_2.draw(window)

    move_x_1 = 1
    move_y_1 = 1
    move_x_2 = 1
    move_y_2 = 1
    while not window.checkMouse():
        circle_1.move(move_x_1, move_y_1)
        circle_2.move(move_x_2, move_y_2)
        time.sleep(.001)
        if hit_vertical(circle_1, window):
            move_y_1 = move_y_1 * -1
        elif hit_horizontal(circle_1, window):
            move_x_1 = move_x_1 * -1
        elif hit_vertical(circle_2, window):
            move_y_2 = move_y_2 * -1
        elif hit_horizontal(circle_2, window):
            move_x_2 = move_x_2 * -1
        elif did_collide(circle_1, circle_2):
            move_x_1 = move_x_1 * -1
            move_y_1 = move_y_1 * -1
            move_x_2 = move_x_2 * -1
            move_y_2 = move_y_2 * -1

    window.close()


bumper()