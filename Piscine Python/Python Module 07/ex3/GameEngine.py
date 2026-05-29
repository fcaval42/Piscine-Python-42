# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 14:51:41 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:13:08 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turn = 0
        self.damage_dealt = 0
        self.hand_size = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        print(f"Factory: {self.factory.name}")
        self.strategy = strategy
        print(f"Strategy: {self.strategy.name}")

    def simulate_turn(self) -> dict:
        self.turn += 1
        return {
            "Turn number": self.turn
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turn,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.damage_dealt,
            "cards_created": self.hand_size
        }
