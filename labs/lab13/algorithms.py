"""
Name: Thomas Scola
algorithms.py
Problem: to form a program that performs a selection sort
Certification of Authenticity:
I received help from the CSL lab with Brooke Duvall
"""

from graphics import*
def read_data(filename):
    #filename = open("data_sorted.txt", "r")
    line = filename.readline().strip()
    empty_list = []
    while line:
        line_list = line.split()
        length = len(line_list)
        i = 0
        while i < length:
            empty_list.append(line_list[i])
            i += 1
        line = filename.readline().strip()
    return empty_list

def is_in_linear(search_val, values):
    length = len(values)
    i = 0
    while i < length:
        if search_val == values[i]:
            return True
        i += 1
    return False

def selection_sort(values):
    n = len(values)

    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1, n):
            if values[i] < values[mp]:
                mp = i
        values[bottom], values[mp] = values[mp], values[bottom]


def rect_sort(rectangles):
    list_rectangles = len(rectangles)

    for bottom in range(list_rectangles - 1):
        mp = bottom
        for i in range(bottom + 1, list_rectangles):
            if calc_area(rectangles[i]) < calc_area(rectangles[mp]):
                mp = i
        rectangles[bottom], rectangles[mp] = rectangles[mp], rectangles[bottom]

def calc_area(rect):
    width = rect.getP2().getX()-rect.getP1().getX()
    length = rect.getP2().getY()-rect.getP1().getY()
    area = width * length
    return area

def main():
    rect1 = Rectangle(Point(1, 2), Point(5, 6))
    rect2 = Rectangle(Point(3, 2), Point(10, 12))
    rect3 = Rectangle(Point(4, 7), Point(20, 24))

    list = []
    list.append(rect3)
    list.append(rect2)
    list.append(rect1)
    rect_sort(list)
    print(list)