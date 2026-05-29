# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:14:16 by fcaval          #+#    #+#               #
#  Updated: 2026/01/23 11:25:47 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import math


def calcul_coordinates(spawn1: list, spawn2: list) -> int:
    x1, y1, z1 = spawn1
    x2, y2, z2 = spawn2

    distance = math.sqrt(
        (x2-x1)**2 +
        (y2-y1)**2 +
        (z2-z1)**2
    )

    return round(distance, 2)


def create_coordinates(coordinates: str) -> tuple:
    try:
        x, y, z = coordinates.split(",")
        return int(x), int(y), int(z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}")\n')


def create_system() -> None:
    print("=== Game Coordinate System ===\n")

    spawn = (0, 0, 0)
    coordinates = (10, 20, 5)
    print(f"Position created: {coordinates}")
    distance = calcul_coordinates(spawn, coordinates)
    print(f"Distance between {spawn} and {coordinates}: {distance}\n")

    coordinates2 = "3,4,0"
    coordinates_split = create_coordinates(coordinates2)
    print(f'Parsing coordinates: "{coordinates2}"')
    print(f"Parsed position: {coordinates_split}")
    distance2 = calcul_coordinates(spawn, coordinates_split)
    print(f"Distance between {spawn} and {coordinates_split}: {distance2}\n")

    coordinates3 = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{coordinates3}"')
    create_coordinates(coordinates3)

    print("Unpacking demonstration:")
    x, y, z = coordinates_split
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}\n")


create_system()
