# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/21 18:39:11 by fcaval          #+#    #+#               #
#  Updated: 2026/01/21 20:04:36 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import sys


def print_args() -> None:
    print("\n=== Command Quest ===\n")

    if len(sys.argv) == 1:
        print("No argument provided!")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {len(sys.argv)}\n")


print_args()
