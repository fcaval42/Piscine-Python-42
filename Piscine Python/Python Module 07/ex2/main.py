# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 16:51:05 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:12:54 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex2.EliteCard import EliteCard


def main():

    print("\n=== DataDeck Ability System ===\n")

# ************************************************************************* #
#                              EliteCard                                    #
# ************************************************************************* #

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

# ************************************************************************* #
#                             Combat phase                                  #
# ************************************************************************* #

    lugia = EliteCard("Lugia_ex", 6, "Special", 180, 150)
    ho_oh = EliteCard("Ho-oh_ex", 2, "Immersive", 80, 150)
    airmure = EliteCard("Airmure_ex", 2, "Full-art", 70, 140)

    print(f"Playing {lugia.name} (Elite Card):\n")
    print("Combat phase:")
    print(f"Attack result: {lugia.attack('Enemy')}")
    print(f"Defense result: {lugia.defend(ho_oh.attack_power)}")
    print()

# ************************************************************************* #
#                              Magic phase                                  #
# ************************************************************************* #

    print("Magic phase:")
    tmp = lugia.cast_spell('Explosion Élémentaire', [ho_oh.name, airmure.name])
    print(f"Spell cast: {tmp}")
    print(f"Mana channel: {lugia.channel_mana(9)}")
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
