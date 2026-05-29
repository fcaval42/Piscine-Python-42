# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 16:52:15 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:12:44 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.mana = 9

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name
        }

# ************************************************************************* #
#                              Combatable                                   #
# ************************************************************************* #

    def attack(self, target) -> dict:
        try:
            if self.mana >= self.cost:
                info_attack = {}
                info_attack["attacker"] = self.name
                info_attack["target"] = target
                info_attack["damage"] = self.attack_power
                info_attack["combat_type"] = "turn-based combat"
                return info_attack
        except ValueError:
            print("You don't have enough mana to attack")

    def defend(self, incoming_damage: int) -> dict:
        info_defend = {}
        try:
            if incoming_damage < self.health:
                info_defend["defender"] = self.name
                info_defend["damage_taken"] = self.health - incoming_damage
                info_defend["damage_blocked"] = 0
                info_defend["still_alive"] = True
                return info_defend
        except ValueError:
            print(f"{self.name} is ko")
            return

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

# ************************************************************************* #
#                                Magical                                    #
# ************************************************************************* #

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        info_spell = {}
        try:
            if self.mana > 0:
                info_spell["caster"] = self.name
                info_spell["spell"] = spell_name
                info_spell["targets"] = targets
                info_spell["mana_used"] = self.cost
                self.mana -= self.cost
            return info_spell
        except ValueError:
            print("You don't have enough mana to attack")

    def channel_mana(self, amount: int) -> dict:
        info_mana = {}
        info_mana["channeled"] = amount - self.cost
        info_mana["total_mana"] = amount
        return info_mana

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }
