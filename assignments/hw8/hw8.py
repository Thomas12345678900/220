"""
Name: Thomas Scola
hw8.py

Problem: Implement function manipulation, graphics, and if statements

Certification of Authenticity:
I worked on this assignment with Ethan Kidwell.
"""
from typing import List
from graphics import*
import math

def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10



def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2



def sum_list(nums):
    lens = len(nums)
    num_total = 0
    increment = 0
    for i in range(lens):
        num_total = num_total + nums[increment]
        increment = increment + 1
    return num_total


def to_numbers(nums):
    increment = 0
    for nums_string in nums:
        nums[increment] = float(nums_string)
        increment = increment + 1


def sum_of_squares(nums):
    increment_3 = 0

    for list_element in nums:
        nums_list = list_element.split(',')

        increment = 0
        increment_2 = 0
        nums_total = 0


        nums_len = len(nums_list)

        for nums_string in nums_list:
            nums_list[increment] = float(nums_string)
            increment = increment + 1

        for number in range(nums_len):
            nums_list[number] = nums_list[number] ** 2

        for i in range(nums_len):
            nums_total = nums_total + nums_list[increment_2]
            increment_2 = increment_2 + 1

        nums[increment_3] = nums_total
        increment_3 = increment_3 + 1
    return nums


def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    return False


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    circle_1_center = win.getMouse()
    circumference_point = win.getMouse()
    circle_1_x = (circle_1_center.getX() - circumference_point.getX()) ** 2
    circle_1_y = (circle_1_center.getY() - circumference_point.getY()) ** 2
    radius = math.sqrt(circle_1_x + circle_1_y)
    circle_one = Circle(circle_1_center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    circle_2_center = win.getMouse()
    circumference_point = win.getMouse()
    circle_2_x = (circle_2_center.getX() - circumference_point.getX()) ** 2
    circle_2_y = (circle_2_center.getY() - circumference_point.getY()) ** 2
    radius = math.sqrt(circle_2_x + circle_2_y)
    circle_two = Circle(circle_2_center, radius)
    circle_two.setFill("light blue")
    circle_two.draw(win)

    if did_overlap(circle_one, circle_two):
        overlapped = Text(Point(5,2), "They do overlap")
        overlapped.draw(win)
    no_overlap = Text(Point(5, 2), "They do not overlap")
    no_overlap.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    circle_1_radius = circle_one.getRadius()
    circle_2_radius = circle_two.getRadius()
    circles_radius = circle_1_radius + circle_2_radius
    circle_1_center = circle_one.getCenter()
    circle_2_center = circle_two.getCenter()
    circle_1_x = circle_1_center.getX()
    circle_1_y = circle_1_center.getY()
    circle_2_x = circle_2_center.getX()
    circle_2_y = circle_2_center.getY()
    circle_distance = math.sqrt(((circle_2_x - circle_1_x) ** 2) + ((circle_2_y - circle_1_y) ** 2))
    if circle_distance <= circles_radius:
        return True
    return False

    pass


if __name__ == '__main__':
    pass
