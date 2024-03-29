#!/usr/bin/python3
""" Class Student Module """


class Student:
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        if type(attrs) == list:
            my_dict = {}
            for element in attrs:
                if type(element) != str:
                    break
                else:
                    if element == "first_name":
                        my_dict["first_name"] = self.first_name
                    elif element == "last_name":
                        my_dict["last_name"] = self.last_name
                    elif element == "age":
                        my_dict["age"] = self.age
            return my_dict
        else:
            return self.__dict__
