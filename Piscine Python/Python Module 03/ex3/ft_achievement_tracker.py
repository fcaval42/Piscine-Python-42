# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: Fleur <Fleur@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/23 11:31:19 by fcaval          #+#    #+#               #
#  Updated: 2026/01/27 21:03:18 by Fleur           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.achievements = set()

    def add_achievements(self, *achievements) -> None:
        for achievement in achievements:
            self.achievements.add(achievement)

    def show_info(self) -> None:
        print(f"🌟 Player {self.name} achievements: {self.achievements}\n")


def achievement() -> None:

    print("=== Achievement Tracker System ===\n")

    player1 = Player(input("⚔️  Enter you name, player one! : "))
    player2 = Player(input("⚔️  Hello, who are you player two? : "))
    player3 = Player(input("⚔️  Are you ready player three? : "))

    player1.add_achievements(
        'first_kill',
        'Commute, work, hero',
        'Great powers...',
        'The friendly neighbourhood spider'
    )

    player2.add_achievements(
        'first_kill',
        'Commute, work, hero',
        'I <3 Manhattan',
        'Spider-Man urban'
    )

    player3.add_achievements(
        'Commute, work, hero',
        'Great powers...',
        'I <3 Manhattan',
        'The friendly neighbourhood spider',
        'Parker Industries'
    )

    print()
    player1.show_info()
    player2.show_info()
    player3.show_info()

    print("=== Achievement Analytics ===\n")
    all_achievement = set.union(player1.achievements, player2.achievements,
                                player3.achievements)
    print(f"✌️ All unique achievements: {all_achievement}")
    print(f"🎯 Total unique achievements: {len(all_achievement)}\n")

    commun_achievement = set.intersection(player1.achievements,
                                          player2.achievements,
                                          player3.achievements)
    print(f"🎉 Common to all players: {commun_achievement}")
    rare_achievement = (
        (player1.achievements - player2.achievements - player3.achievements) |
        (player2.achievements - player1.achievements - player3.achievements) |
        (player3.achievements - player1.achievements - player2.achievements)
    )
    print(f"🏆​ Rare achievements (1 player): {rare_achievement}\n")

    diff1 = player1.achievements.intersection(player2.achievements)
    diff2 = player1.achievements.difference(player2.achievements)
    diff3 = player2.achievements.difference(player1.achievements)
    print(f"🤜 Alice vs Bob common: {diff1}")
    print(f"🤜 Alice unique: {diff2}")
    print(f"🤜 Bob unique: {diff3}\n")


if __name__ == "__main__":
    achievement()
