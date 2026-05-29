# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 16:19:21 by fcaval          #+#    #+#               #
#  Updated: 2026/03/09 11:25:47 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    def accumulator(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: any, value: any) -> None:
        vault[key] = value

    def recall(key: any) -> any:
        if key in vault:
            return vault[key]
        else:
            return "Memory not found"
    return {"store": store, "recall": recall}


def main() -> None:
    try:
        print("\n" + "Testing mage counter...")
        count = mage_counter()
        for i in range(1, 4):
            print(f"Call {i}: {count()}")
    except Exception as e:
        print(f"Error: {e}")

    try:
        print("\n" + "Tetsing enchantment factory...")
        flaming = enchantment_factory("Flaming")
        frozen = enchantment_factory("Frozen")
        print(flaming("Amulet"))
        print(frozen("Wand"))
    except Exception as e:
        print(f"Error: {e}")

    try:
        print("\n" + "Testing spell accumulator...")
        accumulator = spell_accumulator(10)
        print(accumulator(0))
        print(accumulator(5))
    except Exception as e:
        print(f"Error: {e}")

    try:
        print('\nTesting memory vault:')
        vault = memory_vault()
        vault['store']('key', 'value')
        print(vault['recall']('key'))
        print(vault['recall']('value'))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
