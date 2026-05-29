# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 12:02:26 by fcaval          #+#    #+#               #
#  Updated: 2026/02/25 13:55:20 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():

    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    plateform = TournamentPlatform()

# ************************************************************************* #
#                             First pokemon                                 #
# ************************************************************************* #

    lokhlass = TournamentCard("lokhlass", 1, "Shiny", 20, 100, 131)
    id_name = plateform.register_card(lokhlass)

    print(f"{lokhlass.name} ({id_name})")
    print("- Interfaces: [Card, Combatable, Rankable]")
    rating_info = lokhlass.get_rank_info()
    for rating in rating_info.values():
        print(f"- Rating: {rating}")
    print(f"- Record: {lokhlass.wins}-{lokhlass.losses}")
    print()

# ************************************************************************* #
#                            Second pokemon                                 #
# ************************************************************************* #

    mew = TournamentCard("mew", 1, "Immersive", 30, 80, 151)
    id_name = plateform.register_card(mew)

    print(f"{mew.name} ({id_name})")
    print("- Interfaces: [Card, Combatable, Rankable]")
    rating_info = mew.get_rank_info()
    for rating in rating_info.values():
        print(f"- Rating: {rating}")
    print(f"- Record: {mew.wins}-{mew.losses}")
    print()

# ************************************************************************* #
#                                Match                                      #
# ************************************************************************* #

    print("Creating tournament match...")
    match_result = plateform.create_match(lokhlass.id, mew.id)
    print(f"Match result: {match_result}")
    print()

# ************************************************************************* #
#                              Tournament                                   #
# ************************************************************************* #

    print("Tournament Leaderboard:")
    lok = lokhlass.get_tournament_stats()
    print(f"1. {lok['name']} - Rating: {lok['rating']} "
          f"({lok['wins']}-{lok['losses']})")
    mew = mew.get_tournament_stats()
    print(f"2. {mew['name']} - Rating: {mew['rating']} "
          f"({mew['wins']}-{mew['losses']})")
    print()

# ************************************************************************* #
#                               Platform                                    #
# ************************************************************************* #

    print("Platform Report:")
    plateform_report = plateform.generate_tournament_report()
    print(plateform_report)
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
