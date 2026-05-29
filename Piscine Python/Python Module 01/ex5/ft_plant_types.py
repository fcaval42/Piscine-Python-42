"""
Auteur : fcaval@student.42lehavre.fr
Date : 12/01/26
"""

"""
    ------- Plant Types -------
    This module demonstrates inheritance by defining a base Plant class
    and specialized subclasses: Flower, Tree, and Vegetable.
"""

"""
|--------------------------------------------------------|
|          Base class for all plant types                |
|--------------------------------------------------------|
"""


class Plant:
    """ Initializes a plant with basic attributes.

        Args:
            name (str): The plant's name
            height (int): Height in centimeters
            age (int): Age in days
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


"""
|--------------------------------------------------------|
|      Flower class - inherits from Plant                |
|--------------------------------------------------------|
"""


class Flower(Plant):
    """
       Initializes a flower with color attribute.

        Args:
            name (str): The flower's name
            height (int): Height in centimeters
            age (int): Age in days
            color (str): The flower's color
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> object:
        super().__init__(name, height, age)

        self.color = color

    """Displays the flower's blooming stage based on age."""
    def bloom(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")
        if (self.age < 0):
            print(f"The {self.name} was not born !!")
        elif (self.age <= 5):
            print(f"The {self.name} is a little baby 🐣")
        elif (self.age > 5 and self.age <= 10):
            print(f"{self.name} is growing well ! 🐥")
        elif (self.age > 10 and self.age <= 20):
            print(f"{self.name} is blooming beautifully !")
        else:
            print(f"{self.name} is dead 🥀")


"""
|--------------------------------------------------------|
|        Tree class - inherits from Plant               |
|--------------------------------------------------------|
"""


class Tree(Plant):
    """
        Initializes a tree with trunk diameter.

        Args:
            name (str): The tree's name
            height (int): Height in centimeters
            age (int): Age in days
            trunk_diameter (int): Trunk diameter in centimeters
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> object:
        super().__init__(name, height, age)

        self.trunk_diameter = trunk_diameter

    """Calculates and displays the shade area provided by the tree"""
    def product_shade(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.trunk_diameter * 1.5} "
              "square meters of shade")


"""
|--------------------------------------------------------|
|     Vegetable class - inherits from Plant              |
|--------------------------------------------------------|
"""


class Vegetable(Plant):
    """
    Initializes a vegetable with harvest season.

    Args:
        name (str): The vegetable's name
        height (int): Height in centimeters
        age (int): Age in days
        harvest_season (str): The harvest season
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str) -> object:
        super().__init__(name, height, age)

        self.harvest_season = harvest_season.capitalize()

    """ Displays nutritional information based on harvest season."""
    def nutritional_value(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        if (self.harvest_season == "Winter"):
            print(f"The {self.name} did not contain any vitamins ❄️")
        elif (self.harvest_season == "Spring"):
            print(f"The {self.name} creating vitamins 🐝")
        elif (self.harvest_season == "Summer"):
            print(f"{self.name} is rich in vitamin C! 🌻")
        elif (self.harvest_season == "Automn"):
            print(f"The {self.name} is dying 🍂")
        else:
            print(f"{self.harvest_season} is not a season!")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")
    plant1 = Flower("Rose", 25, 5, "red")
    plant1.bloom()
    print("")

    plant2 = Tree("Oak", 500, 1825, 50)
    plant2.product_shade()
    print("")

    plant3 = Vegetable("Tomato", 80, 90, "spring")
    plant3.nutritional_value()
    print("")
