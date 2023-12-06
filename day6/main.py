import os

TEST = False

FILE = "test.txt" if TEST else "input.txt"


with open(os.path.join(os.path.dirname(__file__), FILE)) as f:
    data = f.read().splitlines()

def solve(time, dist):
    r = 0
    for x in range(time + 1):
        d = x * (time - x)
        if d > dist:
            r += 1
    return r


def part_1(data):
    times = list(map(int, data[0].split(":")[1].split()))
    dists = list(map(int, data[1].split(":")[1].split()))

    res = 1
    for time, dist in zip(times,dists):
        res *= solve(time, dist)
    return res

def part_2(data):
    time = int("".join(data[0].split(":")[1].split()))
    dist = int("".join(data[1].split(":")[1].split()))

    return solve(time, dist)

print(part_1(data))
print(part_2(data))