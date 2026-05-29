"""
Auteur : fcaval@student.42lehavre.fr
Date : 07/01/26
"""

"""
    ------- Plant Factory -------
    This module defines a Plant class and demonstrates automated
    plant creation from a list of plant data.
"""

"""
|--------------------------------------------------------|
|  Class representing a plant created from factory data  |
|--------------------------------------------------------|
"""


class Plant:

    """
        Initializes a new plant with given attributes.

        Args:
            name (str): The plant's name
            height (int): Height in centimeters
            age (str): Age in days
    """
    def __init__(self, name: str, height: int, age: str) -> None:
        self.name = name
        self.height = height
        self.age = age

    """Displays the plant creation information"""
    def info(self):
        print(f"Created : {self.name} ({self.height}cm, {self.age} days)")


garden = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]

if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    count = 0
    for name, height, age in garden:
        new_garden = Plant(name, height, age)
        new_garden.info()
        count += 1

    print(f"\nTotal plants created: {count}")
