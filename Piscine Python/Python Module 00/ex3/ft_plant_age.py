"""
Auteur : fcaval@student.42lehavre.fr
Date : 05/01/26
"""


def ft_plant_age():
    age = int(input("Enter plant age in days : "))

    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")
