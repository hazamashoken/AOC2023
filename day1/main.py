import os
import re

TEST = False

FILE = "test.txt" if TEST else "input.txt"

with open(os.path.join(os.path.dirname(__file__), FILE)) as f:
    data = f.read().splitlines()

# Part 1

def part_1(data):
    sum = 0

    for i in range(len(data)):
        numbers = re.findall(r"\d+", data[i])
        first = str(numbers[0])[0]
        last = str(numbers[-1])[-1]
        sum += int(first + last)


    return sum

# Part 2
PATTERN = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))', re.IGNORECASE)

NUMBER_DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9" :9
}

def part_2(data):
    total = 0

    for i in range(len(data)):
        matches = PATTERN.findall(data[i])
        total += int(str(NUMBER_DICT[matches[0]]) + str(NUMBER_DICT[matches[-1]]))
    return total


print(part_1(data))
print(part_2(data))