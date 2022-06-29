def uppercase(str):
    for lower in str:
        upper = ord(lower) + 32
        print("{:c}".format(upper), end='')
        print("\n")

