# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: Fleur <Fleur@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/25 16:20:35 by Fleur           #+#    #+#               #
#  Updated: 2026/01/27 21:05:21 by Fleur           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import sys


def parse_inventory(args) -> dict:
    inventory = dict()
    for arg in args:
        if ':' in arg:
            item, quantity = arg.split(':')
            inventory[item] = int(quantity)
    return inventory


def statistics(inventory) -> list:
    moderate = dict()
    scarce = dict()

    for item, quantity in inventory.items():
        if quantity >= 4:
            moderate[item] = quantity
        else:
            scarce[item] = quantity
    return moderate, scarce


def main() -> None:

    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py "
              "item1:qty item2:qty\n")
        return

    print()
    print("=== Inventory System Analysis ===\n")
    inventory = parse_inventory(sys.argv)
    total_items = sum(inventory.values())
    print(f"Total item in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")
    for item, quantity in sorted(inventory.items(), key=lambda x: x[1],
                                 reverse=True):
        pourcent = quantity * 100 / total_items
        print(f"{item}: {quantity} units ({pourcent:.1f}%)")

    print()
    print("=== Iventory statistics ===")
    max_units = 0
    for item, quantity in inventory.items():
        if quantity > max_units:
            max_units = quantity
            max_item = item
    print(f"Most abudant: {max_item} ({max_units} units)")
    min_units = None
    for item, quantity in inventory.items():
        if min_units is None or quantity < min_units:
            min_units = quantity
            min_item = item
    print(f"Least abundant: {min_item} ({min_units} unit)")

    print()
    print("=== Item Categories=== ")
    moderate, scarce = statistics(inventory)
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print()
    print("=== Management Suggestions ===")
    list_tmp = []
    for item, quantity in inventory.items():
        if quantity < 2:
            list_tmp.append(item)
    print(f"Restock needed: {list_tmp}")

    print()
    print("=== Dictionary Properties Demo ===")
    keys_tmp = list(inventory.keys())
    print(f"Dictionary keys: {keys_tmp}")
    values_tmp = list(inventory.values())
    print(f"Dictionary values: {values_tmp}")
    print("Sample lookup - 'sword' in inventory:", inventory.get("sword")
          is not False)
    print()


main()
