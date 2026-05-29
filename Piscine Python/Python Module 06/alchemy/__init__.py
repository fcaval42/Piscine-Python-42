# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 10:25:22 by fcaval          #+#    #+#               #
#  Updated: 2026/02/17 16:54:16 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .elements import create_fire, create_water

__all__ = [
    "create_fire",
    "create_water"
]
