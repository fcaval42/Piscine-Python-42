# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 10:35:29 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:12:23 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if (self.card.name == card_name):
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        try:
            return self.cards.pop(0)
        except IndexError:
            print("There are no more cards")
            return

    def get_deck_stats(self) -> dict:
        deck_stats = {
            "total_cards": len(self.cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0
            }
        total_cost = 0
        for card in self.cards:
            if isinstance(card, CreatureCard):
                deck_stats["creatures"] += 1
            elif isinstance(card, SpellCard):
                deck_stats["spells"] += 1
            elif isinstance(card, ArtifactCard):
                deck_stats["artifacts"] += 1
            total_cost += card.cost

        if deck_stats["total_cards"] > 0:
            deck_stats["avg_cost"] = round(total_cost /
                                           deck_stats["total_cards"])

        return deck_stats
