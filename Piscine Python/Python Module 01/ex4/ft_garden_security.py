"""
Auteur : fcaval@student.42lehavre.fr
Date : 07/01/26
"""

"""
    ------- Garden Security -------
    This module defines a SecurePlant class that protects
    plant attributes using private variables and validation.
"""

"""
|--------------------------------------------------------|
|   Class with secure access to plant attributes via     |
|              getters and setters                       |
|--------------------------------------------------------|
"""


class SecurePlant:
    """
        Initializes a secure plant with protected attributes.

        Args:
            name (str): The plant's name
            height (int): Initial height in centimeters
            age (int): Initial age in days
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    """Gets the plant's height. Return height in int"""
    def get_height(self) -> int:
        return self.__height

    """Sets the plant's height with validation"""
    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    """Gets the plant's age."""
    def get_age(self) -> int:
        return self.__age

    """Sets the plant's age with validation."""
    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    """Displays the plant's current secure information"""
    def get_info(self):
        print(f"Current plant: {self.name} ({self.get_height()}cm,"
              f" {self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 10, 10)
    print(f"Plant created: {plant.name}")

    plant.set_height(25)
    plant.set_age(30)

    print("")

    plant.set_height(-5)
    "plant.set_age = -6"

    print("")
    plant.get_info()
