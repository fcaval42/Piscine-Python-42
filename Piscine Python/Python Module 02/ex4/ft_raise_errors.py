# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 13:09:58 by fcaval          #+#    #+#               #
#  Updated: 2026/01/21 14:49:10 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


"""Validate plant health parameters and raise errors for invalid values."""


def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    try:
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        if water_level < 1:
            raise ValueError(f"Water lever {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Water lever {water_level} "
                             "is too hight (max 10)")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             "is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             "is too hight (max 12)")
    except ValueError as e:
        print(f"Error : {e}")

    return f"Plant '{plant_name}' is healthy!"


"""Test plant health checker with valid and invalid parameters."""


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    print(check_plant_health("Tomato", 2, 5))
    print()

    print("Testing empty plant name...")
    check_plant_health("", 6, 10)
    print()

    print("Testing bad water level...")
    check_plant_health("tomato", 12, 10)
    print()

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 2, 1)
    print()

    print("All error raising tests completed!")


test_plant_checks()
