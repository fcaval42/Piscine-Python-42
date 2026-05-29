# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 13:00:10 by fcaval          #+#    #+#               #
#  Updated: 2026/03/06 15:19:22 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import List


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(target) -> tuple:
        result1 = spell1(target)
        result2 = spell2(target)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(arg) -> int:
        result = base_spell(arg)
        return result * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditional(mana: int) -> str:
        if condition(mana):
            return spell(mana)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(arg) -> List[str]:
        results = []
        for spell in spells:
            results.append(spell(arg))
        return results
    return sequence


# =========================================================================== #


def Fireball(target: str) -> str:
    return f"Fireball hits {target}"


def Heal(target: str) -> str:
    return f"Heals {target}"


def damage(value: int) -> str:
    return value


def is_dragon(target: str) -> bool:
    return target == "Dragon"


def main() -> None:
    print("\n" + "Testing spell combiner...")
    combined = spell_combiner(Fireball, Heal)
    print("     Combined spell result:", *combined("Dragon"))

    print("\n" + "Testing power amplifier...")
    big_damage = power_amplifier(damage, 6)
    print(f"    Original: {damage(10)}, Amplified: {big_damage(10)}")

    print("\n" + "Testing conditional caster...")
    conditional_spell = conditional_caster(is_dragon, Fireball)
    print("     ", conditional_spell("Dragon"))
    print("     ", conditional_spell("Goblin"))

    print("\n" + "Testing spell sequence...")
    sequence = spell_sequence([Fireball, Heal])
    print("     ", *sequence("Knight"))


if __name__ == "__main__":
    main()
