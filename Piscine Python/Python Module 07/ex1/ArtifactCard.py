# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 10:35:33 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:12:21 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, durability:
                 int, effect: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        play_info = {}
        play_info["card_played"] = self.name
        play_info["mana_used"] = self.cost
        play_info["effect"] = self.effect
        return play_info

    def activate_ability(self) -> dict:
        return {
            "artifact": self.name,
            "effect_activated": self.effect,
            "durability_remaining": self.durability
        }
