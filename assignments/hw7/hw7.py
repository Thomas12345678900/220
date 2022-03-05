"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    i = 0
    for line in in_file:
        for word in line.split():
            i = i + 1
            print((str(i) + " " +word), file=out_file)
    in_file.close()
    out_file.close()
    print(out_file)

def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        word = line.split()
        pay = float(word[2])
        bonus = 1.65
        pay_sum = pay + bonus
        hour = float(word[3])
        total_pay = hour * pay_sum
        print(("{}{}{}{}{:.2f}".format(word[0], " ",word[1]," ", total_pay)), file=out_file)
    in_file.close()
    out_file.close()
    print(out_file)


def calc_check_sum(isbn):
    isbn = isbn.replace("-", "")
    check_num = []
    for i in range(10, 0, -1):
        check_num = check_num + [i]
    total = 0
    for i in range(len(isbn)):
        part = int(isbn[i]) * check_num[i]
        total = total + part
    return total


def send_message(file_name, friend_name):
    in_file = open(file_name, 'r')
    friend_name_file = friend_name + ".txt"
    friend_file = open(friend_name_file, 'w')
    file = in_file.read()
    file = file.strip()
    print(file, file=friend_file)



def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, 'r')
    friends_text = friend_name + ".txt"
    out_file = open(friends_text, 'w')
    encrypted_message = ""
    for line in in_file.readlines():
        encrypted_line = encode(line.rstrip(), key)
        encrypted_message = encrypted_message + encrypted_line + "\n"
    print(encrypted_message.rstrip(), file=out_file)



def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_file_name = open(file_name, 'r')
    in_pad_file = open(pad_file_name, 'r')
    friend_file = friend_name + '.txt'
    better_friend = open(friend_file, 'w')
    message_read = in_file_name.read()
    key_for_reading = in_pad_file.read()
    uncrackable = encode_better(message_read, key_for_reading)
    print(uncrackable, file=better_friend)


if __name__ == '__main__':
    pass
