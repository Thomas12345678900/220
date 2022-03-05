def encode(message, key):
    length_message = len(message)
    encoded_message = ""
    for i in range(length_message):
        letter = message[i]
        encoder = ord(letter) + key
        message_formed = chr(encoder)
        encoded_message = encoded_message + message_formed
    return encoded_message

def encode_better(better_message, better_key):
    cipher_list = []
    answer_list = []
    for message in range(len(better_message) - len(better_key)):
        better_key = better_key + (better_key[message % len(better_key)])
    for letter in range(len(better_message)):
        s_hift = ((ord(better_message[letter])-65) + (ord(better_key[letter])-65)) % 58
        s_hift = s_hift + ord('A')
        cipher_list.append(s_hift)
    for number in range(len(cipher_list)):
        better_decoder = chr(cipher_list[number])
        answer_list.append(better_decoder)
    better_encoded_message = ''.join(answer_list)
    return better_encoded_message