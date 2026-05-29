# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  basic.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 14:51:03 by fcaval          #+#    #+#               #
#  Updated: 2026/02/17 16:55:40 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return (f"Lead transmuted to gold using {create_fire()}")


def stone_to_gem() -> str:
    return (f"Stone transmuted to gem using {create_earth()}")
