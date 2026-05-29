"""
Auteur : fcaval@student.42lehavre.fr
Date : 05/01/26
"""


def ft_water_reminder():
    water = int(input("Days since last watering: "))

    if water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
