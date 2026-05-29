# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  alien_contact.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 11:50:32 by fcaval          #+#    #+#               #
#  Updated: 2026/03/04 15:36:12 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError(" Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and\
           self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(" Strong signals (> 7.0) should "
                             "include received messages")
        return self


def main() -> None:
    print("\n" + "Alien Contact Log Validation".center(79, " "))
    print("".center(79, "="))

    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2019-09-20T10:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="'Greetings from Zeta Reticuli'"
        )
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witness: {alien.witness_count}")
        print(f"Message: {alien.message_received}")

        print("\n" + "".center(79, "="))

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2019-09-20T10:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="'Greetings from Zeta Reticuli'"
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
