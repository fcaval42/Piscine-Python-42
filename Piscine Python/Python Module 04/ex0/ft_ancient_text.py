# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:30:02 by fcaval          #+#    #+#               #
#  Updated: 2026/02/03 13:17:19 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file}")

    try:
        print("Connection established...\n")
        file = open('ancient_fragment.txt', 'r')
        content = file.read()
        print("RECOVERED DATA:")
        print(content)
        print()
        file.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
