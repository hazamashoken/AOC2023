import os
import re
import copy

TEST = False

FILE = "test.txt" if TEST else "input.txt"

BAG_CONFIG = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open(os.path.join(os.path.dirname(__file__), FILE)) as f:
    data = f.read().splitlines()

def part_1(data):
    total = 0

    for line in data:
        valid = True
        id, rounds = int(re.findall(r"\d+", line.split(":")[0])[0]), line.split(":")[-1].split(";")
        for round in rounds:
            bag = copy.deepcopy(BAG_CONFIG)
            hands = round.strip().split(",")
            for hand in hands:
                count, color = hand.strip().split(" ")
                bag[color] -= int(count)

            for value in bag.values():
                if value < 0:
                    valid = False
        if valid:
            total += id

    return total

# Part 2

def part_2(data):
    total = 0

    for line in data:
        bag = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        rounds = line.split(":")[-1].split(";")
        for round in rounds:
            game_total = 1
            hands = round.strip().split(",")
            for hand in hands:
                count, color = hand.strip().split(" ")
                bag[color] = max(int(count), bag[color])

        for value in bag.values():
            game_total *= value
        total += game_total

    return total


print(part_1(data))
print(part_2(data))
