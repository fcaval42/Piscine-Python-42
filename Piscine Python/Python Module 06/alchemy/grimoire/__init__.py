# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 09:42:41 by fcaval          #+#    #+#               #
#  Updated: 2026/02/18 11:34:41 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .spellbook import record_spell
from .validator import validate_ingredients

all = [
    record_spell,
    validate_ingredients
]
