# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 15:44:41 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:01:51 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")

# ************************************************************************* #
#                         Abstract Base class                               #
# ************************************************************************* #

    print("Testing Abstract Base Class Design:")
    try:
        pikachu_ex = CreatureCard('Pikachu', 5, 'Legendary', 30, 120)
        celebi_ex = CreatureCard('Celebi', 7, 'Full-art ex', 50, 130)
    except ValueError as e:
        print(f"Error : {e}")
        return
    print()

# ************************************************************************* #
#                           CreatureCard info                               #
# ************************************************************************* #

    print("CreatedCard Info:")
    print(pikachu_ex.get_card_info())
    print()

# ************************************************************************* #
#                               Play result                                 #
# ************************************************************************* #

    energy = 6
    game_state = {}
    print(f"Playing {pikachu_ex.name} with {energy} energy available:")
    result_playable = pikachu_ex.is_playable(energy)
    print(f"Playable: {result_playable}")
    if result_playable is False:
        print(f"Not enough mana to play {pikachu_ex.name}. Mana available : "
              f"{energy}, and you need {pikachu_ex.cost} for play")
    print(f"Play result: {pikachu_ex.play(game_state)}")
    print()

# ************************************************************************* #
#                                  Attack                                   #
# ************************************************************************* #

    print(f"{pikachu_ex.name} attacks {celebi_ex.name}:")
    attack_info = pikachu_ex.attack_target(celebi_ex)
    print(f"Attack result: {attack_info}")
    print()

# ************************************************************************* #
#                       Insufficient mana                                   #
# ************************************************************************* #

    energy -= pikachu_ex.cost
    print(f"Testing insufficient mana ({energy} available):")
    result_playable = pikachu_ex.is_playable(energy)
    print(f"Playable: {result_playable}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
