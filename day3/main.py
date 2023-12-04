from collections import defaultdict
import os
import re

TEST = False

FILE = "test.txt" if TEST else "input.txt"


with open(os.path.join(os.path.dirname(__file__), FILE)) as f:
    data = f.read()


# Part 1

found = False
lines = []

def flood_find(y, x, width, height):
    if y < 0 or x < 0:
        return
    if y >= height or x >= width:
        return
    if lines[y][x] == '.':
        return
    if lines[y][x] != '.' and not lines[y][x].isdigit():
        global found
        found = True
        return
    lines[y][x] = '.'
    flood_find(y + 1, x, width, height)
    flood_find(y + 1, x + 1, width, height)
    flood_find(y + 1, x - 1, width, height)
    flood_find(y, x - 1, width, height)
    flood_find(y, x + 1, width, height)
    flood_find(y - 1, x, width, height)
    flood_find(y - 1, x + 1, width, height)
    flood_find(y - 1, x - 1, width, height)


def part_1(data: str):

    total = 0
    y = 0
    global lines
    global found
    lines = [ list(lst) for lst in data.splitlines() ]

    numbers = re.findall('[0-9]+', data)
    while y < len(lines) and len(numbers):
        x = ''.join(lines[y]).find(numbers[0])
        if x != -1:
            flood_find(y, x, len(lines[y]), len(lines))
        else:
            y += 1
            continue
        if found == 1:
            total += int(numbers[0])
            found = False
        numbers.pop(0)

    return total


pairs = defaultdict(list)

coor = ()


def flood_star(y, x, width, height):
    global coor
    if y < 0 or x < 0:
        return
    if y >= height or x >= width:
        return
    if lines[y][x] == '.':
        return
    if lines[y][x] == '*' and not lines[y][x].isdigit():
        global found
        found = True
        coor = (y, x)
        return
    lines[y][x] = '.'
    flood_star(y + 1, x, width, height)
    flood_star(y + 1, x + 1, width, height)
    flood_star(y + 1, x - 1, width, height)
    flood_star(y, x - 1, width, height)
    flood_star(y, x + 1, width, height)
    flood_star(y - 1, x, width, height)
    flood_star(y - 1, x + 1, width, height)
    flood_star(y - 1, x - 1, width, height)


def part_2(data: str):
    y = 0
    global lines
    global found
    lines = [ list(line) for line in data.splitlines() ]

    numbers = re.findall('[0-9]+', data)

    while y < len(lines) and len(numbers):
        x = ''.join(lines[y]).find(numbers[0])
        if x != -1:
            flood_star(y, x, len(lines[y]), len(lines))
        else:
            y += 1
            continue
        if found == 1:
            pairs[f"{coor[0]},{coor[1]}"].append(numbers[0])
            found = False
        numbers.pop(0)
    res = []
    for value in pairs.values():
        if len(value) == 2:
            res.append(int(value[0]) * int(value[1]))

    return sum(res)

print(part_1(data))
print(part_2(data))
