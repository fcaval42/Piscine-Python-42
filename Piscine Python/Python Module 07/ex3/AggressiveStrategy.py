# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 14:46:11 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:13:03 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameStrategy import GameStrategy
from random import sample
from ex0.CreatureCard import CreatureCard


class AgressiveStrategy(GameStrategy):

    def __init__(self):
        self.name = "AgressiveStrategy"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        card_choice = sample(hand, 2)
        cards_played = [card.name for card in card_choice]
        mana_sum = sum(card.cost for card in card_choice)
        damage_dealt = sum(card.attack for card in card_choice
                           if isinstance(card, CreatureCard))
        return {
            "card_played": cards_played,
            "mana_used": mana_sum,
            "targets_attacked": "['Pokémon adverse']",
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return f"{self.name}"

    def prioritize_targets(self, available_targets: list) -> list:
        return ['Enemy Player']
