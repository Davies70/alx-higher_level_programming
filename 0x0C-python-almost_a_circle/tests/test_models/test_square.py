#!/usr/bin/python3
'''Unittest for square.py([..])'''
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Define unit test for the Square Class'''
    def test_init(self):
        '''Tests the __init__ function'''
        b1 = Square(1)
        self.assertEqual(b1.id, 1)
        b2 = Square(1, 3, 4)
        self.assertEqual(b2.id, 2)
        b3 = Square(1, 3, 4, 12)
        self.assertEqual(b3.id, 12)
        b4 = Square(1, 3, 4)
        self.assertEqual(b4.id, 3)

    def test_init_fail(self):
        '''Tests the __init__ function'''
        self.assertRaises(TypeError, Square)

    def test_validate_attributes_size_type(self):
        '''Validates the type of size'''
        self.assertRaisesRegex(
            TypeError, 'width must be an integer', Square, '2'
            )

    def test_validate_attributes_size_value(self):
        '''Validates the value of size'''
        self.assertRaisesRegex(
            ValueError, 'width must be > 0', Square, 0
            )

    def test_validate_attributes_x_type(self):
        '''Validates the type of x'''
        self.assertRaisesRegex(
            TypeError, 'x must be an integer', Square, 2, '1'
            )

    def test_validate_attributes_x_value(self):
        '''Validates the value of x'''
        self.assertRaisesRegex(
            ValueError, 'x must be >= 0', Square, 2, -1
            )

    def test_validate_attributes_y_type(self):
        '''Validates the type of y'''
        self.assertRaisesRegex(
            TypeError, 'y must be an integer', Square, 2, 1, '1'
            )

    def test_validate_attributes_y_value(self):
        '''Validates the value of y'''
        self.assertRaisesRegex(
            ValueError, 'y must be >= 0', Square, 2, 1, -1
            )

    def test_area(self):
        '''Tests the area function'''
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

    def test_area_2(self):
        '''Tests the area function'''
        r2 = Square(2)
        self.assertEqual(r2.area(), 4)

    def test_str(self):
        '''Tests the __str__ function'''
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Square] (12) 2/1 - 4')

    def test_str_2(self):
        '''Tests the __str__ function'''
        r2 = Square(5)
        self.assertEqual(r2.__str__(), '[Square] (1) 0/0 - 5')

    def test_update_1(self):
        '''Tests the update function with one value'''
        r1 = Square(10, 10, 10)
        self.assertEqual(r1.__str__(), '[Square] (1) 10/10 - 10')
        r1.update(89)
        self.assertEqual(r1.__str__(), '[Square] (89) 10/10 - 10')

    def test_update_2(self):
        '''Tests the update function with multiple values'''
        r1 = Square(10, 10, 10)
        self.assertEqual(r1.__str__(), '[Square] (1) 10/10 - 10')
        r1.update(89, 2, 4, 5)
        self.assertEqual(r1.__str__(), '[Square] (89) 4/5 - 2')

    def test_update_kwargs_1(self):
        '''Tests the update function with one value'''
        r1 = Square(10, 10, 10)
        self.assertEqual(r1.__str__(), '[Square] (1) 10/10 - 10')
        r1.update(size=1)
        self.assertEqual(r1.__str__(), '[Square] (1) 10/10 - 1')

    def test_update_kwargs_2(self):
        '''Tests the update function with multiple values'''
        print(Square._Base__nb_objects)
        r1 = Square(10, 10, 10)
        self.assertEqual(r1.__str__(), '[Square] (1) 10/10 - 10')
        r1.update(x=1, y=3, size=4, id=89)
        self.assertEqual(r1.__str__(), '[Square] (89) 1/3 - 4')

    def test_to_dictionary(self):
        '''Tests the to_dictionary function with multiple values'''
        r1 = Square(10, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'size': 10})
        self.assertTrue(type(r1_dictionary) is dict)

        r2 = Square(1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r2_dictionary, {'x': 1, 'y': 9, 'id': 1, 'size': 10})
        self.assertNotEqual(r1, r2)

    def test_to_json_string_default(self):
        '''Tests the to_json_string function'''
        r1 = Square(10)
        dictionary = r1.to_dictionary()
        json_dictionary = Square.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)
        self.assertCountEqual(
            json_dictionary, '[{"x": 0, "size": 10, "id": 1, "y": 0}]'
            )

    def test_to_json_string_full(self):
        '''Tests the to_json_string function'''
        r1 = Square(10, 2, 8, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Square.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)
        self.assertCountEqual(
            json_dictionary, '[{"x": 2, "size": 10, "id": 2, "y": 8}]'
            )

    def test_save_to_file(self):
        '''Tests the save_to_file function'''
        r1 = Square(10, 2, 8)
        Square.save_to_file([r1])

        with open("Square.json", "r") as file:
            self.assertCountEqual(
                file.read(), '[{"y": 8, "x": 2, "id": 1, "size": 10}]'
            )

    def test_save_to_file_2(self):
        '''Tests the save_to_file function'''
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])

        with open("Square.json", "r") as file:
            self.assertCountEqual(
                file.read(),
                '[{"y": 8, "x": 2, "id": 1, "size": 10}, \
{"y": 0, "x": 0, "id": 2, "size": 2}]'
            )

    def test_from_json_string(self):
        '''Tests the from_json_string function'''
        list_input = [
            {'id': 89, 'size': 10, 'height': 4},
            {'id': 7, 'size': 1, 'height': 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        '''Tests the create function'''
        r1 = Square(3, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), '[Square] (1) 1/0 - 3')
        self.assertEqual(r2.__str__(), '[Square] (1) 1/0 - 3')
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_from_dict(self):
        '''Tests the create function'''
        r2_dictionary = {'x': 1, 'y': 0, 'size': 3, 'id': 1}
        r2 = Square.create(**r2_dictionary)
        self.assertEqual(r2.__str__(), '[Square] (1) 1/0 - 3')

    def test_load_from_file(self):
        '''Tests the load_from_file function'''
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        list_squares_input = [r1, r2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        i = 0
        for rect in list_squares_output:
            self.assertEqual(list_squares_input[i].__str__(), rect.__str__())
            i += 1

    def tearDown(self):
        Square.del_nb()


if __name__ == '__main__':
    unittest.main()
