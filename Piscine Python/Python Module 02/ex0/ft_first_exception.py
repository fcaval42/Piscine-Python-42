"""
Auteur: fcaval@student.42lehavre.fr
Date: 16/01/2025
"""


"""Check if temperature is valid and within safe range for plants."""


def check_temperature(temp_str) -> int:
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


"""Test temperature checker with various valid and invalid inputs."""


def test_temperature():
    print("=== Garden Temperature Checker ===\n")

    temperature = 25
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = "abc"
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = 100
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = -50
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    print("All tests completed - program didn't crash!")


test_temperature()
