"""
Auteur : fcaval@student.42lehavre.fr
Date : 06/01/26
"""

"""
    ------- Garden's data -------
    This module defines a Plant class and creates instances of plants
    with their basic attributes.
"""

"""
|--------------------------------------------------------|
|    Class representing a plant with basic attributes    |
|--------------------------------------------------------|
"""


class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{Rose.name}: {Rose.height}cm, {Rose.age} days old")
    print(f"{Sunflower.name}: {Sunflower.height}cm, {Sunflower.age} days old")
    print(f"{Cactus.name}: {Cactus.height}cm, {Cactus.age} days old")
