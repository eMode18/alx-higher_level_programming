#!/usr/bin/python3

"""Create a class named base model."""
import json
import csv
import turtle


class Base:
    """Base model class.

    This class serves as the foundation for other classes in the project.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base object.

        Args:
            id (int): The unique identifier for the new Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(obj_list):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            obj_list (list): A list of dictionaries to be serialized.
        """
        if obj_list is None or obj_list == []:
            return "[]"
        return json.dumps(obj_list)

    @classmethod
    def save_to_file(cls, obj_list):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            obj_list (list): A list of inherited Base objects to be serialized.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if obj_list is None:
                json_file.write("[]")
            else:
                obj_dicts = [obj.to_dictionary() for obj in obj_list]
                json_file.write(Base.to_json_string(obj_dicts))

    @staticmethod
    def from_json_string(json_str):
        """Return the deserialization of a JSON string.

        Args:
            json_str (str): A JSON string representation of a list of dictionaries.
        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - the Python list represented by json_str.
        """
        if json_str is None or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **attr_dict):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **attr_dict (dict): Key/value pairs of attributes to initialize.
        """
        if attr_dict and attr_dict != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**attr_dict)
            return new_obj

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from a file named "<cls.__name__>.json".

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as json_file:
                obj_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in obj_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, obj_list):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            obj_list (list): A list of inherited Base objects to be serialized.
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csv_file:
            if obj_list is None or obj_list == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
                for obj in obj_list:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from a file named "<cls.__name__>.csv".

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                obj_dicts = csv.DictReader(csv_file, fieldnames=field_names)
                obj_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in obj_dicts]
                return [cls.create(**d) for d in obj_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(rectangle_list, square_list):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            rectangle_list (list): A list of Rectangle objects to draw.
            square_list (list): A list of Square objects to draw.
        """
        turtle_drawer = turtle.Turtle()
        turtle_drawer.screen.bgcolor("#b7312c")
        turtle_drawer.pensize(3)
        turtle_drawer.shape("turtle")

        # Draw Rectangles in white
        turtle_drawer.color("#ffffff")
        for rectangle in rectangle_list:
            turtle_drawer.showturtle()
            turtle_drawer.up()
            turtle_drawer.goto(rectangle.x, rectangle.y)
            turtle_drawer.down()
            for _ in range(2):
                turtle_drawer.forward(rectangle.width)
                turtle_drawer.left(90)
                turtle_drawer.forward(rectangle.height)
                turtle_drawer.left(90)
            turtle_drawer.hideturtle()

        # Draw Squares in light blue
        turtle_drawer.color("#b5e3d8")
        for square in square_list:
            turtle_drawer.showturtle()
            turtle_drawer.up()
            turtle_drawer.goto(square.x, square.y)
            turtle_drawer.down()
            for _ in range(2):
                turtle_drawer.forward(square.width)
                turtle_drawer.left(90)
                turtle_drawer.forward(square.height)
                turtle_drawer.left(90)
            turtle_drawer.hideturtle()

        turtle.exitonclick()

