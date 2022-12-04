import numpy as np

with open('input.txt', 'r') as f:
    raw = f.read()
rows = raw.split('\n')


def get_parts(pair):
    parts = pair.split(',')
    return tuple(map(lambda x: list(np.array(x).astype(np.int64)), map(lambda x: x.split('-'), parts)))


def is_fully_containing(pair):
    part1, part2 = get_parts(pair)
    return (part1[0] - part2[0]) * (part1[1] - part2[1]) <= 0


print(sum(map(is_fully_containing, rows)))
