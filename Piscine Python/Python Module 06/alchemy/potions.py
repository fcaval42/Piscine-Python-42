# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 11:37:28 by fcaval          #+#    #+#               #
#  Updated: 2026/02/17 16:55:08 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import alchemy.elements as elements


def healing_potion() -> str:
    return (f"Healing potion brewed with {elements.create_fire()} and "
            f"{elements.create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {elements.create_earth()} and "
            f"{elements.create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {elements.create_air()} and "
            f"{elements.create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: {elements.create_fire},"
            f"{elements.create_air}, {elements.create_earth}, "
            f"{elements.create_water}")
