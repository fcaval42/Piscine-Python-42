# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 10:35:11 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:12:28 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        play_info = {}
        play_info["card_played"] = self.name
        play_info["mana_used"] = self.cost
        play_info["effect"] = self.effect_type
        return play_info

    def resolve_effect(self, targets: list) -> dict:
        return {
            "effect_type": self.effect_type,
            "targets_affected": len(targets),
            "resolved": True
        }
