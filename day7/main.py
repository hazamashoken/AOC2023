import os
from collections import Counter

TEST = True

FILE = "test.txt" if TEST else "input.txt"


with open(os.path.join(os.path.dirname(__file__), FILE)) as f:
    data = f.read().splitlines()

def strength(hand: str):
    hand = hand.replace("T", chr(ord('9')+1))
    hand = hand.replace("J", chr(ord('9')+2))
    hand = hand.replace("Q", chr(ord('9')+3))
    hand = hand.replace("K", chr(ord('9')+4))
    hand = hand.replace("A", chr(ord('9')+5))
    
    card_count = Counter(hand)

    if sorted(card_count.values()) == [5]:
        return 10, hand
    elif sorted(card_count.values()) == [1, 4]:
        return 9, hand
    elif sorted(card_count.values()) == [2, 3]:
        return 8, hand
    elif sorted(card_count.values()) == [1, 1, 3]:
        return 7, hand
    elif sorted(card_count.values()) == [1, 2, 2]:
        return 6, hand
    elif sorted(card_count.values()) == [1,1,1,2]:
        return 5, hand
    elif sorted(card_count.values()) == [1,1,1,1,1]:
        return 4, hand
    else:
        assert False, f"{sorted(card_count.values())} {hand}"

def part_1(data):
    score = []
    for line in data:
        hand, bid = line.split()
        score.append((hand, int(bid)))

    score = sorted(score, key=lambda hb: strength(hb[0]))
    res = 0
    for i, (h, b) in enumerate(score):
        res += (i + 1) * b

    return res

def strength2(hand: str):
    hand = hand.replace("J", chr(ord('2')-1))
    hand = hand.replace("T", chr(ord('9')+1))
    hand = hand.replace("Q", chr(ord('9')+3))
    hand = hand.replace("K", chr(ord('9')+4))
    hand = hand.replace("A", chr(ord('9')+5))

    card_count = Counter(hand)
    target = list(card_count.keys())[0]

    for key in card_count:
        if key != '1':
            if card_count[key] > card_count[target] or target=='1':
                target = key
    assert target != '1' or list(card_count.keys()) == ['1']
    if '1' in card_count and target != '1':
        card_count[target] += card_count['1']
        del card_count['1']
    assert '1' not in card_count or list(card_count.keys()) == ['1'], f"{card_count} {hand}"


    if sorted(card_count.values()) == [5]:
        return 10, hand
    elif sorted(card_count.values()) == [1, 4]:
        return 9, hand
    elif sorted(card_count.values()) == [2, 3]:
        return 8, hand
    elif sorted(card_count.values()) == [1, 1, 3]:
        return 7, hand
    elif sorted(card_count.values()) == [1, 2, 2]:
        return 6, hand
    elif sorted(card_count.values()) == [1,1,1,2]:
        return 5, hand
    elif sorted(card_count.values()) == [1,1,1,1,1]:
        return 4, hand
    else:
        assert False, f"{sorted(card_count.values())} {hand}"

def part_2(data):
    score = []
    for line in data:
        hand, bid = line.split()
        score.append((hand, int(bid)))

    score = sorted(score, key=lambda hb: strength2(hb[0]))
    res = 0
    for i, (h, b) in enumerate(score):
        res += (i + 1) * b

    return res

print(part_1(data))
print(part_2(data))