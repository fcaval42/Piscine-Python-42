# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 11:57:33 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 13:38:49 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, rating: int) -> None:
        super().__init__(name, cost, rarity)
        self.rating = rating
        self.attack_power = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.id = None

    def play(self, game_state: dict) -> dict:
        return {
            "card_used": self.name,
            "mana_used": self.cost,
            "rarity": self.rarity
        }

    def attack(self, target) -> dict:
        attack_info = {}
        attack_info["attacker"] = self.name
        attack_info["target"] = target.name
        attack_info["damage"] = self.attack_power
        return attack_info

    def defend(self, incoming_damage: int) -> dict:
        defend_info = {}
        damage_taken = incoming_damage - self.health
        defend_info["defender"] = self.name
        defend_info["damage_taken"] = damage_taken
        if damage_taken >= self.health:
            defend_info["result"] = False
        else:
            defend_info["result"] = True
        return defend_info

    def get_combat_stats(self) -> dict:
        combats_stats = {}
        combats_stats["attack"] = self.attack
        combats_stats["defend"] = self.defend
        combats_stats["health"] = self.health
        return combats_stats

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def calculate_rating(self) -> int:
        if self.wins >= 1:
            self.rating += 50
        elif self.losses >= 1:
            self.rating -= 25

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
