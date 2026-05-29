# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_finally_block.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: fcaval <fcaval@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/19 12:50:59 by fcaval            #+#    #+#             #
#    Updated: 2026/01/19 12:51:44 by fcaval           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

"""Water plants from list and ensure cleanup with finally block."""


def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plants in plant_list:
            plants + "42"
            print(f"Watering {plants}")
    except TypeError:
        print(f"Error: Cannot water {plants} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


"""Test watering system with normal and error scenarios."""


def test_watering_system():
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])

    print("\nCleanup always happens, even with errors!")


test_watering_system()
