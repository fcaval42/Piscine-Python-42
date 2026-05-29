"""
Auteur: fcaval@student.42lehavre.fr
Date: 16/01/2025
"""

"""Demonstrate different types of Python exceptions with examples."""


def garden_operations(Error, value, others) -> None:

    if Error == "Value":
        try:
            test = int(value)
        except ValueError as a:
            print(f"Caught ValueError: {a}\n")

    elif Error == "Zero":
        try:
            test = 10 / value
        except ZeroDivisionError as a:
            print(f"Caught ZeroDivisionError: {a}\n")

    elif Error == "File":
        try:
            test = open(value, 'r')
            test.close()
        except FileNotFoundError as a:
            print(f"Caught FileNotFoundError: {a}\n")

    elif Error == "Key":
        try:
            test = value["camion"]
        except KeyError as a:
            print(f"Caught KeyError: {a}\n")

    elif Error == "Multiple":
        try:
            10 / value
            int(others)
        except (ValueError, ZeroDivisionError):
            print("Caught an error, but program continues!\n")


"""Test various Python exception types with different scenarios."""


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    garden_operations("Value", "abc", None)

    print("Testing ZeroDivisionError...")
    garden_operations("Zero", 0, None)

    print("Testing FileNotFoundError...")
    garden_operations("File", "No.txt", None)

    print("Testing KeyError...")
    dictionary = {
        "voiture": "véhicule à 4 roues",
        "vélo": "véhicule à 2 roues"
    }
    garden_operations("Key", dictionary, None)

    print("Testing multiple errors together...")
    garden_operations("Multiple", 0, "abc")

    print("All error types tested successfully!")


test_error_types()
