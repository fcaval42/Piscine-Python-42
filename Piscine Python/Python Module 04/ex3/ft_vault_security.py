# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 15:39:01 by fcaval          #+#    #+#               #
#  Updated: 2026/02/03 16:41:53 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    try:
        with open('classified_data.txt', 'w') as file:
            file.write("[CLASSIFIED] Quantum encryption keys recovered\n"
                       "[CLASSIFIED] Archive integrity: 100%")

        with open('classified_data.txt', 'r') as file:
            print("SECURE EXTRACTION:")
            content = file.read()
            print(content)

        print()

        with open('security_protocols.txt', 'w') as file:
            file.write("[CLASSIFIED] New security "
                       "protocols archived\nVault automatically sealed upon "
                       "completion")

        with open('security_protocols.txt', 'r') as file:
            print("SECURE PRESERVATION:")
            content2 = file.read()
            print(content2)

        print()
        print("All vault operations completed with maximum security.")

    except FileNotFoundError as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
