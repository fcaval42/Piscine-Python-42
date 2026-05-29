# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 13:43:40 by fcaval          #+#    #+#               #
#  Updated: 2026/03/09 15:19:10 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(operator.add, spells)
    if operation == "multiply":
        return reduce(operator.mul, spells)
    if operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    if operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    else:
        raise ValueError("Operator is impossible")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "light")
    }


@lru_cache(maxsize=50)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(spell) -> str:
        raise NotImplementedError("unknown data")

    @spell.register(int)
    def _(arg):
        return f"Damage spell: {arg}"

    @spell.register(str)
    def _(arg):
        return f"Enchantment: {arg}"

    @spell.register(list)
    def _(arg):
        result = []
        for elem in arg:
            result.append(spell(elem))
        return result

    return spell


def main():
    try:
        print("\nTesting spell reducer...")
        print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
        print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
        print(f"Max: {spell_reducer([10, 20, 30, 40], 'max')}")
        print(f"Min: {spell_reducer([10, 20, 30, 40], 'min')}")
    except Exception as e:
        print(f"ERROR: {e}")

    try:
        def base(power, element, target):
            return f"{element} enchants {target} with {power} power"

        print("\nTesting spell reducer...")
        enchants = partial_enchanter(base)
        print(enchants['fire_enchant'](target="Sword"))
        print(enchants['ice_enchant'](target="Sword"))
        print(enchants['lightning_enchant'](target="Sword"))
    except Exception as e:
        print(f"ERROR: {e}")

    try:
        print("\nTesting memoized fibonacci...")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except Exception as e:
        print(f"ERROR: {e}")

    try:
        print("\nTesting spell dispatcher...")
        spell = spell_dispatcher()
        print(f"{spell(10)}")
        print(f"{spell('fire')}")
        print(f"{spell([10, 'fire'])}")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
