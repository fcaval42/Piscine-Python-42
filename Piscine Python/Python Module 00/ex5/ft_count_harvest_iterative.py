"""
Auteur : fcaval@student.42lehavre.fr
Date : 05/01/26
"""


def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))

    for i in range(1, day + 1):
        print(f"Day : {i}")
    print("Harvest time!")
