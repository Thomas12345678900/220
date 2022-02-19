"""
Name: Thomas Scola
hw5.py

Problem: Write a programs that utilize the basics of strings and lists

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Enter your first and last name: ")

    first_name = name.split()[0]
    last_name = name.split()[1]
    print(last_name + ", " + first_name)  # for printing output string


def company_name():
    domain = input("enter the domain name")
    print(domain[4:-4])

def initials():
    num_students = eval(input("How many students? "))
    for i in range(num_students):
        student_names = input("Enter the first and last names of the students: ")
        first_name = student_names.split()[0]
        last_name = student_names.split()[1]
        print(first_name[0:1], last_name[0:1])


def names():
    names = input("Enter people's names, separated by commas: ")
    name_list = list(names.split(", "))

    for i in name_list:
       list_2 = i.split(" ")
       first_name = list_2[0]
       last_name = list_2[1]
       initial_1 = first_name[0]
       initial_2 = last_name[0]
       initials = initial_1 + initial_2
       print(initials)


def thirds():
    total_sliced = ""
    num_sentences = eval(input("Enter the number of sentences: "))
    for i in range(num_sentences):
        sentence = input("enter sentence")
        sliced = sentence[0::3]
        total_sliced = total_sliced + sliced
    print(total_sliced)

def word_average():
    sentence = input("Enter the sentence")
    sentence_split = sentence.split()
    num_words = len(sentence_split)
    total = 0
    for i in sentence_split:
        length_of_words = len(i)
        total = total + length_of_words
    average = total / num_words
    print(average)

def pig_latin():
    converter_sentence = input("Enter your sentence to be converted: ")
    word_bucket = converter_sentence.split()
    pig_latin = " "
    for i in word_bucket:
        letter_number_one = i[0]
        words = i[1:]
        ay = "ay"
        pig_latin = pig_latin + words + letter_number_one + ay
        pig_latin = pig_latin.lower()
    print(pig_latin.rstrip())

if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
