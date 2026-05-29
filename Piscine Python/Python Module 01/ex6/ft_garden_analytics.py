"""
Auteur : fcaval@student.42lehavre.fr
Date : 13/01/26
"""

"""
    ------- Garden Analytics -------
    This module demonstrates advanced OOP concepts including inheritance,
    nested classes, static methods, and class methods for managing
    multiple gardens with different plant types.
"""

"""
|--------------------------------------------------------|
|          Base class for all plant types               |
|--------------------------------------------------------|
"""


class Plant:
    """
    Initializes a plant with name and height.

    Args:
        name (str): The plant's name
        height (int): Height in centimeters
    """
    def __init__(self, name: str, height: int) -> None:
        self.name = name.capitalize()
        self.height = height

    """ Increases the plant's height by 1 centimeter"""
    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    """Displays basic plant information."""
    def display_info(self):
        print(f"\n- {self.name}: {self.height}cm", end="")

    """Gets and displays plant information."""
    def get_info(self):
        self.display_info()


"""
|--------------------------------------------------------|
|    FloweringPlant class - inherits from Plant         |
|--------------------------------------------------------|
"""


class FloweringPlant(Plant):
    """
    Initializes a flowering plant with color.

    Args:
        name (str): The plant's name
        height (int): Height in centimeters
        color (str): The flower's color
    """
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)

        self.color = color

    """Displays flowering plant information including color."""
    def get_info(self):
        super().display_info()
        print(f", {self.color} flowers (blooming)", end="")


"""
|--------------------------------------------------------|
|   PrizeFlower class - inherits from FloweringPlant    |
|--------------------------------------------------------|
"""


class PrizeFlower(FloweringPlant):
    """
    Initializes a prize flower with prize points.

    Args:
        name (str): The flower's name
        height (int): Height in centimeters
        color (str): The flower's color
        prize_points (int): Prize points value
    """
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)

        self.prize_points = prize_points

    """Displays prize flower information including points."""
    def get_info(self):
        super().display_info()
        print(f", {self.color} flowers (blooming), Prize points :"
              f" {self.prize_points}", end="")


"""
|--------------------------------------------------------|
|          Garden class - manages plant collections     |
|--------------------------------------------------------|
"""


class Garden:
    """
    Manages a collection of plants in a garden.

    Attributes:
        name (str): The garden owner's name
        plants (list): List of all plants in the garden
        regular (int): Count of regular plants
        flowering (int): Count of flowering plants
        prize_flowers (int): Count of prize flowers
        score (int): Total garden score
        total_growing (int): Total growth count
    """

    def __init__(self, name: str):
        self.plants = []
        self.name = name
        self.regular = 0
        self.flowering = 0
        self.prize_flowers = 0
        self.score = 0
        self.total_growing = 0

    """Adds a regular plant to the garden."""
    def add_regular(self, new_plant: Plant):
        self.score += 31
        self.regular += 1
        self.plants.append(new_plant)
        print(f"Added {new_plant.name} to {self.name}'s garden")

    """Adds a flowering plant to the garden."""
    def add_flowering(self, new_plant: Plant):
        self.score += 46
        self.flowering += 1
        self.plants.append(new_plant)
        print(f"Added {new_plant.name} to {self.name}'s garden")

    """Adds a prize flower to the garden."""
    def add_prize_flowers(self, new_plant: Plant):
        self.score += 52
        self.prize_flowers += 1
        self.plants.append(new_plant)
        print(f"Added {new_plant.name} to {self.name}'s garden")

    """Makes all plants in the garden grow."""
    def growing_plant(self) -> int:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growing += 1
        return self.total_growing


"""
|--------------------------------------------------------|
|    GardenManager - manages multiple gardens with      |
|              nested statistics class                   |
|--------------------------------------------------------|
"""


class GardenManager:
    """
    Manages multiple gardens and provides analytics.

    Class Attributes:
        all_manager (list): List of all managed gardens
        total_manager (int): Total number of managed gardens
        total_garden (int): Total number of plants across gardens
    """
    all_manager = []
    total_manager = 0
    total_garden = 0

    """
    |--------------------------------------------------------|
    |     Nested class for garden statistics methods        |
    |--------------------------------------------------------|
    """

    class GardenStats:

        """ Calculates and displays garden statistics."""
        @staticmethod
        def calcul_garden(garden: Garden):
            total_garden = (garden.regular + garden.flowering
                            + garden.prize_flowers)
            GardenManager.total_garden = total_garden
            print(f"\n=== {garden.name}'s Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                plant.get_info()
            return total_garden

        """Validates if a height value is positive."""
        @staticmethod
        def height_validation(height: int) -> bool:
            if height > 0:
                return True
            else:
                return False

    """Registers multiple gardens for management."""
    @classmethod
    def create_garden_network(cls, list_manager):
        for manager in list_manager:
            GardenManager.total_manager += 1
            cls.all_manager.append(manager)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    Alice = Garden("Alice")
    Bob = Garden("Bob")
    GardenManager.create_garden_network([Alice, Bob])
    Alice.add_regular(Plant("Oak Tree", 100))
    Alice.add_flowering(FloweringPlant("Rose", 25, "red"))
    Alice.add_prize_flowers(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()

    """Bob.add_regular(Plant("Oak Tree", 101))"""

    growing = Alice.growing_plant()

    GardenManager.GardenStats.calcul_garden(Alice)
    print(f"\n\nPlants added: {GardenManager.total_garden},"
          f" Total growth: {growing}cm")
    print(f"Plant types: {Alice.regular} regular, "
          f"{Alice.flowering} flowering, "
          f"{Alice.prize_flowers} prize flowers\n")

    print(f"Height validation test: "
          f"{GardenManager.GardenStats.height_validation(10)}")

    score = []
    for garden in GardenManager.all_manager:
        sentance = f"{garden.name}: {garden.score}"
        score.append(sentance)
    result = ", ".join(score)
    print("Garden scores - " + result)

    print(f"Total gardens managed: {GardenManager.total_manager}")
