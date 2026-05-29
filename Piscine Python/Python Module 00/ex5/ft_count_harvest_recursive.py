"""
Auteur : fcaval@student.42lehavre.fr
Date : 05/01/26
"""


def ft_count_harvest_recursive(what=-1):
    if (what == -1):
        day = input("Days until harvest: ")
    else:
        day = what
    if (int(day) > 0):
        ft_count_harvest_recursive(int(day) - 1)
        print(f"Day {day}")
    if (what == -1):
        print("Harvest time!")
