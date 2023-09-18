#!/usr/bin/python3
"""Defines unittests for base.py.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """testing instantiation of the Base class."""

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)


class TestBaseToJsonString(unittest.TestCase):
    """testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        rectangle = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rectangle.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        rectangle = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rectangle.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        rectangle_1 = Rectangle(2, 3, 5, 19, 2)
        rectangle_2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rectangle_1.to_dictionary(), rectangle_2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        square = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([square.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        square = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([square.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        square_1 = Square(10, 2, 3, 4)
        square_2 = Square(4, 5, 21, 2)
        list_dicts = [square_1.to_dictionary(), square_2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveToFile(unittest.TestCase):
    """testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        rectangle = Rectangle(8, 6, 1, 3, 9)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 57)

    def test_save_to_file_two_rectangles(self):
        rectangle_1 = Rectangle(8, 6, 1, 3, 9)
        rectangle_2 = Rectangle(5, 5, 0, 0, 2)
        Rectangle.save_to_file([rectangle_1, rectangle_2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 110)

    def test_save_to_file_one_square(self):
        square = Square(7, 5, 3, 2)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 43)

    def test_save_to_file_two_squares(self):
        square_1 = Square(7, 5, 3, 2)
        square_2 = Square(4, 2, 1, 5)
        Square.save_to_file([square_1, square_2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 85)

    def test_save_to_file_cls_name_for_filename(self):
        square = Square(7, 5, 3, 2)
        Base.save_to_file([square])
        with open("Base.json", "r") as file:
            self.assertTrue(len(file.read()) == 43)

    def test_save_to_file_overwrite(self):
        square_1 = Square(6, 1, 1, 5)
        Square.save_to_file([square_1])
        square_2 = Square(7, 5, 3, 2)
        Square.save_to_file([square_2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 43)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBaseFromJsonString(unittest.TestCase):
    """testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBaseCreate(unittest.TestCase):
    """testing create method of Base class."""

    def test_create_rectangle_original(self):
        rectangle_1 = Rectangle(3, 5, 1, 2, 7)
        rectangle_dict = rectangle_1.to_dictionary()
        rectangle_2 = Rectangle.create(**rectangle_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rectangle_1))

    def test_create_rectangle_new(self):
        rectangle_1 = Rectangle(3, 5, 1, 2, 7)
        rectangle_dict = rectangle_1.to_dictionary()
        rectangle_2 = Rectangle.create(**rectangle_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rectangle_2))

    def test_create_rectangle_is(self):
        rectangle_1 = Rectangle(3, 5, 1, 2, 7)
        rectangle_dict = rectangle_1.to_dictionary()
        rectangle_2 = Rectangle.create(**rectangle_dict)
        self.assertIsNot(rectangle_1, rectangle_2)

    def test_create_rectangle_equals(self):
        rectangle_1 = Rectangle(3, 5, 1, 2, 7)
        rectangle_dict = rectangle_1.to_dictionary()
        rectangle_2 = Rectangle.create(**rectangle_dict)
        self.assertNotEqual(rectangle_1, rectangle_2)

    def test_create_square_original(self):
        square_1 = Square(3, 5, 1, 7)
        square_dict = square_1.to_dictionary()
        square_2 = Square.create(**square_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(square_1))

    def test_create_square_new(self):
        square_1 = Square(3, 5, 1, 7)
        square_dict = square_1.to_dictionary()
        square_2 = Square.create(**square_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(square_2))

    def test_create_square_is(self):
        square_1 = Square(3, 5, 1, 7)
        square_dict = square_1.to_dictionary()
        square_2 = Square.create(**square_dict)
        self.assertIsNot(square_1, square_2)

    def test_create_square_equals(self):
        square_1 = Square(3, 5, 1, 7)
        square_dict = square_1.to_dictionary()
        square_2 = Square.create(**square_dict)
        self.assertNotEqual(square_1, square_2)


class TestBaseLoadFromFile(unittest.TestCase):
    """testing load_from_file method of Base class."""

    @classmethod
    def tearDown(self):
        """remove created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        rectangle_1 = Rectangle(8, 6, 1, 3, 9)
        rectangle_2 = Rectangle(4, 5, 0, 0, 2)
        Rectangle.save_to_file([rectangle_1, rectangle_2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(rectangle_1.__str__(), list_rectangles_output[0].__str__())

    def test_load_from_file_second_rectangle(self):
        rectangle_1 = Rectangle(8, 6, 1, 3, 9)
        rectangle_2 = Rectangle(4, 5, 0, 0, 2)
        Rectangle.save_to_file([rectangle_1, rectangle_2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(rectangle_2.__str__(), list_rectangles_output[1].__str__())

    def test_load_from_file_first_square(self):
        square_1 = Square(7, 5, 3, 2)
        square_2 = Square(3, 2, 1, 1)
        Square.save_to_file([square_1, square_2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(square_1.__str__(), list_squares_output[0].__str__())

    def test_load_from_file_second_square(self):
        square_1 = Square(7, 5, 3, 2)
        square_2 = Square(3, 2, 1, 1)
        Square.save_to_file([square_1, square_2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(square_2.__str__(), list_squares_output[1].__str__())

    def test_load_from_file_no_file(self):
        list_output = Rectangle.load_from_file()
        self.assertEqual([], list_output)

    def test_load_from_file_empty_file(self):
        with open("Rectangle.json", "w") as file:
            file.write("")
        list_output = Rectangle.load_from_file()
        self.assertEqual([], list_output)

    def test_load_from_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([])


if __name__ == '__main__':
    unittest.main()

