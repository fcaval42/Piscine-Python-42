# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 16:23:50 by fcaval          #+#    #+#               #
#  Updated: 2026/01/20 15:34:13 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:

    """Initialize a plant with name, water level, and sunlight hours."""
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water = water_level
        self.sun = sunlight_hours


class GardenManager:

    """Initialize garden manager with empty plants list and water tank."""
    def __init__(self):
        self.plants = []
        self.tank = 10

    """Add a plant to the garden if it has a valid name."""
    def add_plants(self, plant: Plant):
        if plant.name == "":
            print("Error adding plant: Plant name cannot be empty!")
        else:
            print(f"Added {plant.name} successfully")
            self.plants.append(plant)

    """Water all plants in the garden using the water tank."""
    def watering_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.tank < 5:
                    raise WaterError("Not enough water in tank")
                plant.water += 5
                self.tank -= 5
                print(f"Watering {plant.name} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def checking_plants(self):
        try:
            for plant in self.plants:
                if plant.water < 1:
                    raise PlantError(f"Water level {plant.water} is too "
                                     "low (min 1)")
                elif plant.water > 10:
                    raise PlantError(f"Water level {plant.water} is too high "
                                     "(max 10)")
                elif plant.sun < 2:
                    raise PlantError(f"Sunlight level {plant.water} is too "
                                     "low (min 2)")
                elif plant.sun > 12:
                    raise PlantError(f"Sunlight level {plant.water} "
                                     "is too high (max 12)")
                else:
                    print(f"{plant.name}: healthy (water: {plant.water}, "
                          f"sun: {plant.sun})")

        except PlantError as e:
            print(f"Error checking {plant.name} : {e}")

    """Check and refill water tank if level is insufficient."""
    def checking_tank(self):
        try:
            if self.tank < 5:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            while self.tank <= 5:
                self.tank += 5
            print("System recovered and continuing...")


def test_garden_management():
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    garden = GardenManager()
    try:
        garden.add_plants(Plant("tomato", 5, 8))
        garden.add_plants(Plant("lettuce", 15, 8))
        garden.add_plants(Plant("", 5, 8))
    except GardenError as e:
        print(e)
    print()

    print("Watering plants...")
    garden.watering_plants()
    print()

    print("Checking plant health...")
    garden.checking_plants()
    print()

    print("Testing error recovery...")
    garden.checking_tank()
    print()

    print("Garden management system test complete!")


test_garden_management()
