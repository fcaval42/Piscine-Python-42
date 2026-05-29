# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 15:44:34 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:01:44 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        info_play = {}
        info_play["card_played"] = self.name
        info_play["mana_used"] = self.cost
        info_play["effect"] = "The Pokémon is ready to battle"
        return info_play

    def attack_target(self, target) -> dict:
        attack_info = {}
        attack_info["attacker"] = self.name
        attack_info["target"] = target.name
        attack_info["damage_dealt"] = self.attack
        if self.attack >= target.health:
            attack_info["combat_resolved"] = False
        else:
            attack_info["combat_resolved"] = True
        return attack_info

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["Type"] = self.type
        info["attack"] = self.attack
        info["health"] = self.health
        return info
