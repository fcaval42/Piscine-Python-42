# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 09:43:09 by fcaval          #+#    #+#               #
#  Updated: 2026/02/18 11:34:53 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def validate_ingredients(ingredients: str) -> str:
    elements = ['air', 'earth', 'fire', 'water']
    for element in elements:
        if element in ingredients:
            return (f"{ingredients} - VALID")
        else:
            return (f"{ingredients} - INVALID")
