# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 11:37:50 by fcaval          #+#    #+#               #
#  Updated: 2026/02/18 11:35:51 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import alchemy.elements
from alchemy.elements import create_earth
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water
from alchemy.potions import strength_potion as strength


def main():
    print("\n === Inport Transmutation Mastery === \n")

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print()

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")
    print()

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength()}")
    print()

    print("All import transmutation methods mastered!")


main()
