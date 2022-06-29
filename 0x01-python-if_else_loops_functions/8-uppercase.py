#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        character = ord(letter)
        if character >= 97 and character <= 122:
            alpha = character - 32
        else:
            alpha = character
        print("{:c}".format(alpha), end='')
    print("\n")
