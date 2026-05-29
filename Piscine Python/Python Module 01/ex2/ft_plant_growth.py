"""
Auteur : fcaval@student.42lehavre.fr
Date : 07/01/26
"""

"""
    ------- Plant Growth -------
    This module defines a Plant class with methods to simulate
    plant growth over time, tracking height and age changes.
"""

"""
|--------------------------------------------------------|
|  Class representing a plant with growth capabilities   |
|--------------------------------------------------------|
"""


class Plant:
    """Initializes a new plant with basic attributes.

        Args:
            name (str): The plant's name
            height (int): Initial height in centimeters
            age (int): Initial age in days"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    """ Increases the plant's height by 1 centimeter"""
    def grow(self):
        self.height += 1

    """ Increases the plant's age by 1 day."""
    def grow_age(self):
        self.age += 1

    """Displays the plant's current information."""
    def info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    days = 1
    rose = Plant("Rose", 25, 30)
    height_origin = rose.height
    print(f"=== Day {days} ====")
    rose.info()

    for days in range(2, 8):
        rose.grow()
        rose.grow_age()

    print(f"=== Day {days} ===")
    rose.info()
    development = rose.height - height_origin
    print(f"Growth this week : +{development}cm")
