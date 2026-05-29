# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 15:27:59 by fcaval          #+#    #+#               #
#  Updated: 2026/03/10 10:06:29 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def fonction(*args) -> int:
        start = time.time()
        print(f"Casting {func.__name__}...")
        result = func(*args)
        end = time.time()
        print(f"Spell completed in {end - start:.6f} second")
        return result
    return fonction


def power_validator(min_power: int) -> callable:

    def decorator(func):

        @wraps(func)
        def fonction(*args):
            if isinstance(args[0], MageGuild):
                power = args[2]
            else:
                power = args[0]
            if power >= min_power:
                return func(*args)
            else:
                return "Insufficient power for this spell"
        return fonction

    return decorator


def retry_spell(max_attempts: int) -> callable:
    def fonction(func):
        @wraps(func)
        def wrapper(*args, n=1):
            try:
                return func(*args)
            except Exception:
                print(f"Spell failed, retrying... ({n}/{max_attempts})")
                if n < max_attempts:
                    return wrapper(*args, n=n+1)
                else:
                    print("Spell casting failed "
                          f"after {max_attempts} attempts")
                    return None
        return wrapper
    return fonction


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace()
                                  for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    try:
        def fireball() -> str:
            return "Fireball cast!"
        print("\nTesting spell timer...")
        time_spell = spell_timer(fireball)
        print(f"Result: {time_spell()}")
    except Exception as e:
        print(f"ERROR: {e}")

    try:
        @power_validator(10)
        def fireball(power: int) -> str:
            return f"Fireball cast with {power}!"

        print("\nTesting power validator...")
        print(f"{fireball(69)}")
        print(f"{fireball(6)}")
    except Exception as e:
        print(f"ERROR: {e}")

    try:
        @retry_spell(5)
        def fireball(power: int) -> None:
            if power < 0:
                raise Exception("power must be positive")
            else:
                return f"Fireball cast with {power}!"

        print("\nTesting retry spell...")
        spell = fireball(-1)
        if spell:
            print(spell)
    except Exception as e:
        print(f"ERROR: {e}")

    try:
        print("\nTesting MageGuild...")
        guild = MageGuild()
        print(guild.validate_mage_name("Henry"))
        print(guild.validate_mage_name("@jifd33d"))
        print(guild.cast_spell("Lightning", 15))
        print(guild.cast_spell("heal", 9))
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
