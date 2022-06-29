#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        character = ord(letter)
        if character >= 65 and character <= 95:
            alpha = character
        elif character >= 97 and character <= 122:
            alpha = character - 32
        elif character == 32:
            alpha = 32
        elif character >=48 and character <= 57:
            alpha = character
        print("{:c}".format(alpha), end='')
    print("\n")
