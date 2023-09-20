#!/usr/bin/python3
"""Defines unittests for models/square.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcdefg'))


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"a": 1, "b": 2})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, memoryview(b'abcdefg'))


class TestSquare_area(unittest.TestCase):
    """Unittests for testing area method of the Square class."""

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_args(self):
        with self.assertRaises(TypeError):
            Square(5, 2).area(5)

    def test_area_kwargs(self):
        with self.assertRaises(TypeError):
            Square(5, 2).area(size=5)

    def test_area_extra_args(self):
        with self.assertRaises(TypeError):
            Square(5, 2).area(5, 10)

    def test_area_extra_kwargs(self):
        with self.assertRaises(TypeError):
            Square(5, 2).area(size=5, extra=10)


class TestSquare_display(unittest.TestCase):
    """Unittests for testing display method of the Square class."""

    def test_display_stdout(self):
        expected_output = "\n" * 2 + "#" * 5 + "\n" * 2
        s = Square(5)
        with io.StringIO() as buffer, redirect_stdout(buffer):
            s.display()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_display_stdout_x(self):
        expected_output = " " * 2 + "#" * 5 + "\n"
        s = Square(5, 2)
        with io.StringIO() as buffer, redirect_stdout(buffer):
            s.display()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_display_stdout_y(self):
        expected_output = "\n" * 2 + "\n" * 2 + "#" * 5 + "\n"
        s = Square(5, 0, 2)
        with io.StringIO() as buffer, redirect_stdout(buffer):
            s.display()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_display_stdout_x_y(self):
        expected_output = " " * 2 + "\n" * 2 + "#" * 5 + "\n"
        s = Square(5, 2, 2)
        with io.StringIO() as buffer, redirect_stdout(buffer):
            s.display()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_display_args(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.display(5)

    def test_display_kwargs(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.display(size=5)

    def test_display_extra_args(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.display(5, 10)

    def test_display_extra_kwargs(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.display(size=5, extra=10)


class TestSquare_str(unittest.TestCase):
    """Unittests for testing str method of the Square class."""

    def test_str_empty(self):
        s = Square(5)
        expected_output = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(s), expected_output)

    def test_str_full(self):
        s = Square(5, 2, 3, 10)
        expected_output = "[Square] (10) 2/3 - 5"
        self.assertEqual(str(s), expected_output)

    def test_str_args(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.__str__(5)

    def test_str_kwargs(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.__str__(size=5)

    def test_str_extra_args(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.__str__(5, 10)

    def test_str_extra_kwargs(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.__str__(size=5, extra=10)


class TestSquare_update(unittest.TestCase):
    """Unittests for testing update method of the Square class."""

    def test_update_args_id(self):
        s = Square(5, 2)
        s.update(1)
        self.assertEqual(s.id, 1)

    def test_update_args_size(self):
        s = Square(5, 2)
        s.update(1, 10)
        self.assertEqual(s.size, 10)

    def test_update_args_x(self):
        s = Square(5, 2)
        s.update(1, 10, 3)
        self.assertEqual(s.x, 3)

    def test_update_args_y(self):
        s = Square(5, 2)
        s.update(1, 10, 3, 5)
        self.assertEqual(s.y, 5)

    def test_update_args_all(self):
        s = Square(5, 2)
        s.update(1, 10, 3, 5, 100)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_update_args_negative_size(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(1, -10)

    def test_update_args_negative_x(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(1, 10, -3)

    def test_update_args_negative_y(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(1, 10, 3, -5)

    def test_update_args_extra_args(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.update(1, 10, 3, 5, 100, 200)

    def test_update_kwargs_id(self):
        s = Square(5, 2)
        s.update(id=1)
        self.assertEqual(s.id, 1)

    def test_update_kwargs_size(self):
        s = Square(5, 2)
        s.update(size=10)
        self.assertEqual(s.size, 10)

    def test_update_kwargs_x(self):
        s = Square(5, 2)
        s.update(x=3)
        self.assertEqual(s.x, 3)

    def test_update_kwargs_y(self):
        s = Square(5, 2)
        s.update(y=5)
        self.assertEqual(s.y, 5)

    def test_update_kwargs_all(self):
        s = Square(5, 2)
        s.update(id=1, size=10, x=3, y=5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_update_kwargs_negative_size(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(size=-10)

    def test_update_kwargs_negative_x(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(x=-3)

    def test_update_kwargs_negative_y(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(y=-5)

    def test_update_args_kwargs_id(self):
        s = Square(5, 2)
        s.update(1, id=10)
        self.assertEqual(s.id, 1)

    def test_update_args_kwargs_size(self):
        s = Square(5, 2)
        s.update(1, 10, size=20)
        self.assertEqual(s.size, 10)

    def test_update_args_kwargs_x(self):
        s = Square(5, 2)
        s.update(1, 10, 3, x=30)
        self.assertEqual(s.x, 3)

    def test_update_args_kwargs_y(self):
        s = Square(5, 2)
        s.update(1, 10, 3, 5, y=50)
        self.assertEqual(s.y, 5)

    def test_update_args_kwargs_all(self):
        s = Square(5, 2)
        s.update(1, 10, 3, 5, 100, id=200, size=20, x=30, y=50)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_update_args_kwargs_negative_size(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(1, -10, size=20)

    def test_update_args_kwargs_negative_x(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(1, 10, 3, x=-30)

    def test_update_args_kwargs_negative_y(self):
        s = Square(5, 2)
        with self.assertRaises(ValueError):
            s.update(1, 10, 3, 5, y=-50)

    def test_update_args_kwargs_extra_args(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.update(1, 10, 3, 5, 100, 200, size=20, x=30, y=50)

    def test_update_args_kwargs_invalid_arg(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.update(1, 10, 3, 5, invalid=100)

    def test_update_args_kwargs_invalid_kwarg(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.update(1, 10, 3, 5, invalid=100)

    def test_update_args_kwargs_invalid_arg_kwarg(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.update(1, 10, 3, 5, 100, invalid=200)


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_empty(self):
        s = Square(5)
        expected_output = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected_output)

    def test_to_dictionary_full(self):
        s = Square(5, 2, 3, 10)
        expected_output = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_output)

    def test_to_dictionary_args(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.to_dictionary(5)

    def test_to_dictionary_kwargs(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.to_dictionary(size=5)

    def test_to_dictionary_extra_args(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.to_dictionary(5, 10)

    def test_to_dictionary_extra_kwargs(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.to_dictionary(size=5, extra=10)


if __name__ == '__main__':
    unittest.main()

