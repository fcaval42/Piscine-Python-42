# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 09:44:29 by fcaval          #+#    #+#               #
#  Updated: 2026/03/06 12:54:58 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import List

artifacts = [{'name': 'Light Prism', 'power': 77, 'type': 'armor'},
             {'name': 'Wind Cloak', 'power': 108, 'type': 'relic'},
             {'name': 'Light Prism', 'power': 84, 'type': 'accessory'},
             {'name': 'Shadow Blade', 'power': 78, 'type': 'focus'}]
mages = [{'name': 'Ash', 'power': 82, 'element': 'earth'},
         {'name': 'Phoenix', 'power': 91, 'element': 'wind'},
         {'name': 'Ash', 'power': 66, 'element': 'ice'},
         {'name': 'Kai', 'power': 83, 'element': 'earth'},
         {'name': 'Alex', 'power': 79, 'element': 'shadow'}]
spells = ['shield', 'fireball', 'freeze', 'blizzard']


def artifact_sorter(artifacts: List[dict]) -> List[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[dict], min_power: int) -> List[dict]:
    return list(filter(lambda x: (x['power'] >= min_power), mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: List[dict]) -> dict:
    powers = list(map(lambda x: x['power'], mages))

    return {
        "most_power": max(powers),
        "least_power": min(powers),
        "avg_power": round(sum(powers)/len(powers), 2)
    }


def main() -> None:
    print("\n" + "Testing artifact sorter...")

    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(*transformed)

    print("\n" + "BONUS".center(65, "="))

    print("Testing power filter...")
    mages_filtered = power_filter(mages, 80)
    for mage in mages_filtered:
        print(f"{mage['name']} ({mage['power']})")
    print()

    print("\n""Testing mage_stats")
    mages_stats = mage_stats(mages)
    print(mages_stats)


if __name__ == "__main__":
    main()
