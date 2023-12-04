import os


TEST = False

FILE = "test.txt" if TEST else "input.txt"


with open(os.path.join(os.path.dirname(__file__), FILE)) as f:
    data = f.read().splitlines()

def part_1(data):
    total = 0
    for line in data:
        score = 0
        wining, cards = line.split(":")[-1].split("|")
        wining = wining.split()
        cards = cards.split()
        for card in cards:
            if card in wining:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total += score

    return total

def part_2(data):
    card_dict = {n: 1 for n in  range(1, len(data) + 1)}
    for n, line in enumerate(data, 1):
        score = 0
        wining, cards = line.split(":")[-1].split("|")
        wining = wining.split()
        cards = cards.split()
        for card in cards:
            if card in wining:
                score += 1
        for i in range(1, score + 1):

            if n + i in card_dict.keys():
                card_dict[n + i] += 1 * card_dict[n]
            else:
                card_dict[n + i] = 1

    return sum(card_dict.values())

print(part_1(data))
print(part_2(data))

# 1, 2, 4 ,8, 14, 1