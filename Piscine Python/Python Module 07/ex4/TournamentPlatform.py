# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 12:00:32 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 13:53:59 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard


class TournamentPlatform():

    def __init__(self):
        self.card = {}
        self.matches_played = 0
        self.total_card = 0
        self.rating1 = 0
        self.rating2 = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"ID: {card.name}_{len(self.card) + 1:03d}"
        card.id = card_id
        self.card[card_id] = card
        self.total_card += 1
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.card[card1_id]
        card2 = self.card[card2_id]

        self.rating1 = card1.rating
        self.rating2 = card2.rating

        attack_result = card1.attack(card2)
        defend_result = card2.defend(attack_result["damage"])

        winner = None
        loser = None
        if defend_result["result"] is False:
            winner = card2.name
            loser = card1.name
            card2.update_wins(1)
            card1.update_losses(1)
            card1.calculate_rating()
            card2.calculate_rating()
        elif defend_result["result"] is True:
            winner = card1.name
            loser = card2.name
            card1.update_wins(1)
            card2.update_losses(1)
            card1.calculate_rating()
            card2.calculate_rating()

            self.matches_played += 1

        return {
            "winner": winner,
            "loser": loser,
            "winner_rating": card1.rating,
            "loser_rating": card2.rating
        }

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        return {
            "total_cards": self.total_card,
            "matches_played": self.matches_played,
            "avg_rating": round((self.rating1+self.rating2)/2),
            "plateform_status": "active"
        }
