# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 14:54:17 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:13:12 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AgressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")

# ************************************************************************* #
#                           Configuring Card                                #
# ************************************************************************* #

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AgressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)
    print(f"Available types: {factory.get_supported_types()}")
    print()

# ************************************************************************* #
#                                Hand                                       #
# ************************************************************************* #

    print("Simulating aggressive turn...")
    pokemon1 = factory.create_creature()
    pokemon2 = factory.create_creature()
    pokemon3 = factory.create_spell()

    hand = [pokemon1, pokemon2, pokemon3]
    print(f"Hand: {[f'{card.name} ({card.cost})' for card in hand]}")
    print()

# ************************************************************************* #
#                            Turn execution                                 #
# ************************************************************************* #

    print("Turn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    action = strategy.execute_turn(hand, [])
    print(f"Actions: {action}")
    print()

# ************************************************************************* #
#                              Game report                                  #
# ************************************************************************* #

    engine.simulate_turn()
    print("Game Report:")
    action = strategy.execute_turn(hand, [])
    engine.damage_dealt = action['damage_dealt']
    engine.hand_size = len(hand)
    status = engine.get_engine_status()
    print(f"{status}")
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
