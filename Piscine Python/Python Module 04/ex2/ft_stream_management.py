# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 13:51:34 by fcaval          #+#    #+#               #
#  Updated: 2026/02/03 15:31:21 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        archivist = input('Input Stream active. Enter archivist ID: ')
        status = input('Input Stream active. Enter status report: ')
        print()
        sys.stdout.write(f"[STANDARD] Archive status from {archivist}: "
                         f"{status}\n")
        sys.stderr.write("[ALERT] System diagnostic: Communication channels "
                         "verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        print()
        print("Three-channel communication test successful.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
