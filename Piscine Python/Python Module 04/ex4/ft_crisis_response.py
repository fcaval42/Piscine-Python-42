# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 11:44:12 by fcaval          #+#    #+#               #
#  Updated: 2026/02/04 13:40:37 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file = ['lost_archive.txt', 'classified_data.txt', 'standard_archive.txt']

    for files in file:
        try:
            with open(files, 'r') as f:
                print(f"ROUTINE ACCESS: Attempting access to '{files}'...")
                print(f"SUCESS:  Archive recovered - '{f.read()}'")

            print("STATUS: Normal operations resumed")

        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{files}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")

        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{files}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")

        print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
