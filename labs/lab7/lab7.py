"""
Name: Thomas Scola
lab7.py
Problem: create a program that reads text files and calculate weight averages
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):

    weighted_averages_list = []

    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name)

    print("\n###-- " + in_file_name + " --###\n")

    for line in in_file:
        all_values = line.split()
        grades = []
        weights = []
        weighted_average = 0

        for i in range(2, len(all_values), 2):
            num_weight = eval(all_values[i])
            weights.append(num_weight)

        for i in range(3, len(all_values), 2):
            num_grade = eval(all_values[i])
            grades.append(num_grade)

        for i in range(len(grades)):
            weighted_average = ((weights[i]) * (grades[i])) + weighted_average
        final_weight_average = weighted_average / 100
        weighted_averages_list.append(final_weight_average)
        print(all_values[0] + " " + all_values[1] + "'s average: {0:.1f}".format(final_weight_average))

    total_average_weighted = (sum(weighted_averages_list) / len(weighted_averages_list))

    print("Class Average: ", total_average_weighted)
    in_file.close()
    out_file.close()

weighted_average("grade.txt", "out.txt")

#test.txt