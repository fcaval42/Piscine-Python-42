# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 10:12:41 by fcaval          #+#    #+#               #
#  Updated: 2026/03/02 15:59:26 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os
import site


def main() -> None:
    try:
        if sys.prefix == sys.base_prefix:
            print("\nMATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environnement: None detected")
            print()

            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install")
            print()

            print("To enter the construct, run:")
            print("python3 -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts activate # On Windows")
            print()

            print("Then run this program again.")
        else:
            print("\nMATRIX STATUS: Welcome to the construct\n")

            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environnement: {os.path.basename(sys.prefix)}")
            print(f"Environnement Path: {sys.prefix}")
            print()

            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting "
                  "the global system.")
            print()

            print(f"Package installation path: {site.USER_SITE}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
