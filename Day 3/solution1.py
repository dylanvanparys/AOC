import string

with open('input.txt', 'r') as f:
    raw = f.read()
rows = raw.split('\n')


def get_compartments(rucksack):
    return rucksack[:len(rucksack) // 2:], rucksack[len(rucksack) // 2::]


def get_priority_char(char):
    if char.isupper():
        return 1 + 26 + string.ascii_uppercase.index(char)
    return 1 + string.ascii_lowercase.index(char)


def get_common_item(part1, part2):
    return next(iter(set(part1).intersection(set(part2))))


def get_priority(rucksack):
    part1, part2 = get_compartments(rucksack)
    return get_priority_char(get_common_item(part1, part2))


priorities = list(map(get_priority, rows))
print(sum(priorities))
