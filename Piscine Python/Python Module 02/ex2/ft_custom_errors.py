"""
Auteur: fcaval@student.42lehavre.fr
Date: 19/01/2025
"""


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


"""Demonstrate custom exception handling for garden errors."""


def custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    test = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]
    for all_error in test:
        try:
            raise all_error
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print()
    print("All custom error types work correctly!")


custom_errors()
