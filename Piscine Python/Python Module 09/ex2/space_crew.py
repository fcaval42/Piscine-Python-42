# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_crew.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 10:00:52 by fcaval          #+#    #+#               #
#  Updated: 2026/03/04 15:35:40 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    cadet = "cadet"
    officer = "officier"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        commander_or_captain = False
        for member in self.crew:
            if member.rank == Rank.captain or member.rank == Rank.commander:
                commander_or_captain = True
            if not member.is_active:
                raise ValueError("All crew members must be active")
        if not commander_or_captain:
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")
        if self.duration_days > 365:
            experiences = len([m for m in self.crew
                               if m.years_experience > 5])
            if experiences/len(self.crew) < 0.5:
                raise ValueError("Long missions (> 365 days) need "
                                 "50% experienced crew (5+ years)")
        return self


def main() -> None:
    print("\n" + "Space Mission Crew Validation".center(79, " "))
    print("".center(79, "="))

    try:
        mission = SpaceMission(
            mission_id="M2024_TITAN",
            mission_name="Solar Observatory Research Mission",
            destination="Solar Observatory",
            launch_date="2024-03-30T00:00:00",
            duration_days=451,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Williams",
                    rank=Rank.captain,
                    age=43,
                    specialization="Mission Command",
                    years_experience=19,
                    is_active=True),
                CrewMember(
                    member_id="CM002",
                    name="James Hernandez",
                    rank=Rank.captain,
                    age=43,
                    specialization="Pilot",
                    years_experience=30,
                    is_active=True),
                CrewMember(
                    member_id="CM003",
                    name="Anna Jones",
                    rank=Rank.cadet,
                    age=35,
                    specialization="Communications",
                    years_experience=15,
                    is_active=True)
            ])

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) - "
                  f"{member.specialization}")

        print("\n" + "".center(79, "="))

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    try:
        mission = SpaceMission(
            mission_id="M2024_TITAN",
            mission_name="Solar Observatory Research Mission",
            destination="Solar Observatory",
            launch_date="2024-03-30T00:00:00",
            duration_days=451,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Williams",
                    rank=Rank.cadet,
                    age=43,
                    specialization="Mission Command",
                    years_experience=19,
                    is_active=True),
            ])

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
