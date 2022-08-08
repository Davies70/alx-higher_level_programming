#!/usr/bin/python3
'''Unittest for base.py([..])'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Define unit test for the Base Class'''
    def test_init(self):
        '''Tests the __init__ function'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        '''Tests the to_json_string function'''
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)
        self.assertEqual(
            json_dictionary,
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
            )

    def test_from_json_string(self):
        '''Tests the from_json_string function'''
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)
        self.assertEqual(list_input, list_output)


if __name__ == '__main__':
    unittest.main()
