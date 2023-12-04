import os
import re
import copy

TEST = True

FILE = "test.txt" if TEST else "input.txt"

BAG_CONFIG = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open(os.path.join(os.path.dirname(__file__), FILE)) as f:
    data = f.read().splitlines()

total = 0

# Part 1

for line in data:
    valid = True
    id, rounds = int(re.findall(r"\d+", line.split(":")[0])[0]), line.split(":")[-1].split(";")
    for round in rounds:
        bag = copy.deepcopy(BAG_CONFIG)
        hands = round.strip().split(",")
        for hand in hands:
            count, color = hand.strip().split(" ")
            bag[color] -= int(count)

        for key, value in bag.items():
            if value < 0:
                valid = False
    if valid:
        total += id

# Part 2