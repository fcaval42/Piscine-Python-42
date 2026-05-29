# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: Fleur <Fleur@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/26 17:06:03 by Fleur           #+#    #+#               #
#  Updated: 2026/01/27 21:06:33 by Fleur           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
import time


def game_event_chance(event_count: str):

    players = ["alice", "bob", "charlie", "arthur", "lana"]
    event = ["killed monster", "found treasure", "leveled up"]

    for i in range(event_count):
        yield {
            "player": random.choice(players),
            "level": random.randint(1, 20),
            "event_type": random.choice(event)
        }


def count_event(events) -> int:
    count = 0
    for event in events:
        count += 1
    return count


def fibonnaci():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


def is_prime(n) -> bool:
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def primes():
    num = 2
    while 1:
        if is_prime(num):
            yield num
        num += 1


def main() -> None:
    print("\n=== Game Data Stream Processor ===\n")
    start_time = time.time()

    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    just_few_events = game_event_chance(event_count)
    for i in range(3):
        event = next(just_few_events)
        print(f"Event {i}: Player {event['player']} "
              f"(level {event['level']}) {event['event_type']}")
    print("...\n")

    print("=== Stream Analytics ===")
    event = game_event_chance(event_count)
    total = count_event(event)
    print(f"Total events processed: {total}")

    events = game_event_chance(event_count)
    high_level_players = 0
    for event in events:
        if event["level"] >= 10:
            high_level_players += 1
    print(f"High-level players (10+): {high_level_players}")

    events = game_event_chance(event_count)
    treasure = 0
    for event in events:
        if event['event_type'] == "found treasure":
            treasure += 1
    print(f"Treasure events: {treasure}")

    events = game_event_chance(event_count)
    level_up = 0
    for event in events:
        if event['event_type'] == "leveled up":
            level_up += 1
    print(f"Level_up events: {level_up}")
    print()

    print("Memory usage: Constant (streaming)")
    end_time = time.time()
    print(f"Processing time: {(end_time - start_time):.3f} seconds\n")

    print("=== Generator Demonstration ===")
    result_fibonacci = fibonnaci()
    print("Fibonnaci sequence (first 10): ", end="")
    for i in range(10):
        print(f"{next(result_fibonacci)} ", end="")
    print()

    print("Prime numbers (first 5): ", end="")
    result_prime = primes()
    for i in range(5):
        print(f"{next(result_prime)} ", end="")
    print("\n")


main()
