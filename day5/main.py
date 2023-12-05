import os
from functools import reduce

TEST = False

FILE = "test.txt" if TEST else "input.txt"


with open(os.path.join(os.path.dirname(__file__), FILE)) as f:
    data = f.read().split("\n\n")

def lookup(value, mapping):
    _, *ranges = mapping.split("\n")
    for r in ranges:
        dst, src, n = map(int, r.split())
        if src <= value < src + n:
            return value - src + dst
    return value

def part_1(data):

    seeds = data[0].split()[1:]
    return min(reduce(lookup, data, int(s)) for s in seeds)


def lookup2(lo, hi, mapping):
    res = []
    for mp in mapping:
        src_lo, dest, rng = mp
        src_hi = src_lo + rng - 1
        if lo < src_lo:
            if hi < src_lo:
                res.append((lo, hi))
                return res
            res.append((lo, src_lo-1))
            lo = src_lo
        if lo > src_hi:
            continue
        if hi <= src_hi:
            res.append((lo - src_lo + dest, hi - src_lo + dest))
            return res
        res.append((lo - src_lo + dest, src_hi - src_lo + dest))
        lo = src_hi + 1

    res.append((lo, hi))
    return res

def part_2(data):
    raw_seeds = [*map(int, data[0].split()[1:])]
    seeds = [(raw_seeds[i], raw_seeds[i]+raw_seeds[i+1]-1) for i in range(0, len(raw_seeds)-1, 2)]
    mappings = [sorted([[int(line.split()[i]) for i in [1,0,2]] for line in mp.strip().split('\n')[1:]]) for mp in data[1:]]

    def find_min(pair, map_level):
        mapping = mappings[map_level]
        lo, hi = pair
        ranges = lookup2(lo, hi, mapping)
        if map_level == len(mappings) - 1:
            return ranges[0][0]
        return min([find_min(pair, map_level+1) for pair in ranges])

    return(min([find_min(pair, 0) for pair in seeds]))

print(part_1(data))
print(part_2(data))
