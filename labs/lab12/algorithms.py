"""
Name: Thomas Scola
algorithms.py
Problem: to form a proggram that reads a file and does linear search for a value
Certification of Authenticity:
I received help from the CSL lab with Brooke Duvall
"""
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
