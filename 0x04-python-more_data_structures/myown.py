#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
       size = len(roman_string)
        sum_list = []
        if (size == 1):
            if roman_string == 'I':
                return (1)
            if roman_string[i] == 'V':
                sum_list.append(5)
            if roman_string[i] == 'X':
                sum_list.append(10)
            if roman_string[i] == 'L':
                sum_list.append(50)
            if roman_string == 'C':
                return (100)
            if roman_string[i] == 'D':
                return (500)
            if roman_string == 'M':
                return (1000)

        for i in range(9):
            if roman_string[i] == 'I' and roman_string[i + 1] == 'X':
                sum_list.append(9)
            if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
                sum_list.append(4)
            if roman_string[i] == 'X' and roman_string[i + 1] == 'L':
                sum_list.append(40)
            if roman_string[i] == 'X' and roman_string[i + 1] == 'C':
                sum_list.append(90)
            if roman_string[i] == 'C' and roman_string[i + 1] == 'D':
                sum_list.append(400)
            if roman_string[i] == 'C' and roman_string[i + 1] == 'M':
                sum_list.append(900)
            else:
                if roman_string[i] == 'I':
                    sum_list.append(1)
                if roman_string[i] == 'V':
                    sum_list.append(5)
                if roman_string[i] == 'X':
                    sum_list.append(10)
                if roman_string[i] == 'L':
                    sum_list.append(50)
                if roman_string[i] == 'C':
                     sum_list.append(100)
                if roman_string[i] == 'D':
                    sum_list.append(500)
                if roman_string[i] == 'M':
                     sum_list.append(1000)
        number = 0
        for j in sum_list:
            number += j
        return number





