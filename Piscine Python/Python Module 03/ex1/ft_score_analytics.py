# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: Fleur <Fleur@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/21 18:59:16 by fcaval          #+#    #+#               #
#  Updated: 2026/01/30 12:09:15 by Fleur           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import sys


def score_analytics() -> None:
    score = []

    print("\n=== Player Score Analytics ===\n")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...\n")
        return

    try:
        for i in range(1, len(sys.argv)):
            score.append(int(sys.argv[i]))
    except ValueError:
        print("Invalid score ⚔️\n")
        return

    print(f"📊 Scores processed: {score}")
    print(f"😎 Total players: {len(score)}")
    print(f"👑 Total score: {sum(score)}")
    print(f"🌟 Average score: {sum(score) / len(score)}")
    print(f"🔥 High score: {max(score)}")
    print(f"📢 Low score: {min(score)}")
    print(f"🏆 Score range: {max(score) - min(score)}\n")


score_analytics()
