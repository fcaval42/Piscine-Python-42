# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 09:42:17 by fcaval          #+#    #+#               #
#  Updated: 2026/02/18 11:35:20 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def main():
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print("validate_ingredients('fire air'): "
          f"{validate_ingredients('fire air')}")
    print("validate_ingredients('dragon scales'): "
          f"{validate_ingredients('dragon scales')}")
    print()

    print("Testing spell recording with validation:")
    print("record_spell('Fireball', 'fire air): "
          f"{record_spell('Fireball', 'fire air')}")
    print("record_spell('Dark magic', 'shadow'): "
          f"{record_spell('Dark Magic', 'shadow')}")
    print()

    print("Testing late import technique:")
    print("record_spell('Lightning', 'air'): "
          f"{record_spell('Lightning', 'air')}")
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
