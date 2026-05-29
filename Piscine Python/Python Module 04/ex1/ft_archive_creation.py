# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 13:21:52 by fcaval          #+#    #+#               #
#  Updated: 2026/02/03 13:57:30 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    print("Storage unit created successfully...\n")

    try:
        print("Inscribing preservation data...")
        file = open('new_discovery.txt', 'r+')
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        file.seek(0)
        content = file.read()
        print(content)
        file.close()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")

    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
