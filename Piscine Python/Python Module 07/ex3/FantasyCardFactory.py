# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 14:48:20 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 14:13:06 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card
from random import sample, choice


class FantasyCardFactory(CardFactory):

    data = {
        "creatures": {
            "Pyroli": CreatureCard("Pyroli_ex", 5, "Rare", 130, 150),
            "Nymphali": CreatureCard("Nymphali_ex", 3, "Full-art", 70, 140),
            "Évoli": CreatureCard("Évoli_ex", 1, "Immersive", 30, 90),
            "Phyllali": CreatureCard("Phyllali", 1, "Commun", 10, 90),
            "Voltali": CreatureCard("Voltali", 1, "Commun", 40, 90),
            "Aquali": CreatureCard("Aquali", 4, "Commun", 70, 120),
            "Mentali": CreatureCard("Mentali", 1, "Commun", 20, 100),
            "Givrali": CreatureCard("Givrali", 3, "Shiny", 90, 140),
            "Noctali": CreatureCard("Noctali", 2, "Commun", 40, 100)
        },
        "spell": {
           "Danse Flammes": SpellCard("Danse Flammes", 5, "Rare", "Feu"),
           "Vent féérique": SpellCard("Vent féérique", 3, "Rare", "Fée"),
           "Entrave Sombre": SpellCard("Entrave Sombre", 1, "Commun",
                                       "Ténèbres"),
           "Morsure": SpellCard("Morsure", 1, "Commun", "Normal")
        },
        "artifact": {
            "Sac Evoli": ArtifactCard("Sac évoli", 3, "Gold", 1, "+20 dégâts"),
            "Restes": ArtifactCard("Restes", 1, "Commun", 2, "+10 soins"),
            "PokéBall": ArtifactCard("PokéBall", 1, "Commun", 1,
                                     "piocher une carte")
        }
    }

    def __init__(self):
        self.name = "FantasyCardFactory"

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creature_name = choice(list(self.data["creatures"].keys()))
        creature = self.data["creatures"][creature_name]
        return creature

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spell_name = choice(list(self.data["spell"].keys()))
        spell = self.data["spell"][spell_name]
        return spell

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifact_name = choice(list(self.data["artifact"].keys()))
        artifact = self.data["artifact"][artifact_name]
        return artifact

    def create_themed_deck(self, size: int) -> dict:
        return {
            "Type Fée": "Fée",
            "Type Électrique": "Électrique",
            "Type Plante": "Plante",
            "Type Feu": "Feu",
            "Type Ténèbres": "Ténèbres",
            "Type Eau": "Eau"
        }

    def get_supported_types(self) -> dict:
        available_type = {}
        available_type["creatures"] = sample(
            list(self.data["creatures"].keys()), 2)
        available_type["spell"] = sample(list(self.data["spell"].keys()), 1)
        available_type["artifact"] = sample(
            list(self.data["artifact"].keys()), 1)
        return available_type
