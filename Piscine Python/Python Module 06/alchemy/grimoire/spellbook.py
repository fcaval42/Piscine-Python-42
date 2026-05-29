# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 09:42:51 by fcaval          #+#    #+#               #
#  Updated: 2026/02/18 11:34:49 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validate = validate_ingredients(ingredients)
    if "INVALID" in validate:
        return (f"Spell rejected: {spell_name} ({validate})")
    else:
        return (f"Spell recorded: {spell_name} ({validate})")
