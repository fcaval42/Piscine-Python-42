# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 10:35:45 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:12:25 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():

    print("\n=== DataDeck Deck Builder ===\n")

# ************************************************************************* #
#                              Building deck                                #
# ************************************************************************* #

    print("Building deck with different card types...")

    deck = Deck()

    try:
        creature = CreatureCard("Nymphali_ex", 3, "Shiny", 70, 140)
        spell = SpellCard("Vent féérique", 2, "Common", "Psy and normal")
        artifact = ArtifactCard("Ruban du bonheur", 2, "Rare", 1,
                                "you may draw 2 cards")
    except ValueError as e:
        print(f"Error: {e}")
        return

    card_list = [creature, spell, artifact]
    for card in card_list:
        deck.add_card(card)

    print(f"Deck stats: {deck.get_deck_stats()}")
    print()

# ************************************************************************* #
#                            Playing Spell                                  #
# ************************************************************************* #

    energy = 8
    print("Drawing and playing cards:")
    print()
    deck.shuffle()
    try:
        while deck.cards:
            draw = deck.draw_card()

            if isinstance(draw, SpellCard):
                card_type = "Spell"
            elif isinstance(draw, ArtifactCard):
                card_type = "Artifact"
            elif isinstance(draw, CreatureCard):
                card_type = "Creature"
            print(f"Drew: {draw.name} ({card_type})")
            play_info = draw.play(energy)
            if play_info:
                print(f"Play result: {play_info}")
            print()
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
