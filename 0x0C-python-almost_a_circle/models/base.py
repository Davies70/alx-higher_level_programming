#!/usr/bin/python3
""" base module """


import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes JSON representation of list_objs to file'''
        filename = f'{cls.__name__}.json'

        if list_objs is None:
            with open(filename, 'w', encoding='utf-8') as f:
                pass
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                buf = []
                for i in list_objs:
                    dictionary = i.to_dictionary()
                    buf.append(dictionary)
                    json_buf = Base.to_json_string(buf)
                    f.write(json_buf)

    @classmethod
    def create(cls, **dictionary):
        '''Creates an instance of a class'''
        if cls.__name__ == 'Rectangle':
            inst = cls(1, 1)
        elif cls.__name__ == 'Square':
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances from a JSON file'''
        filename = f'{cls.__name__}.json'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                json_string = f.read()
                list_of_dict = cls.from_json_string(json_string)
                list_of_inst = []
                for i in list_of_dict:
                    inst = cls.create(**i)
                    list_of_inst.append(inst)
                return list_of_inst
        except FileNotFoundError:
            return []

    @staticmethod
    def from_json_string(json_string):
        '''Returns list of dictionaries from JSON string'''
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def del_nb(cls):
        '''Resets the value of nb'''
        Base.__nb_objects = 0
