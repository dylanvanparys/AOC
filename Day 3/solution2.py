import string

with open('input.txt', 'r') as f:
    raw = f.read()
rows = raw.split('\n')


def get_priority_char(char):
    if char.isupper():
        return 1 + 26 + string.ascii_uppercase.index(char)
    return 1 + string.ascii_lowercase.index(char)


def get_common_item(part1, part2, part3):
    return next(iter(set(part1).intersection(set(part2)).intersection(set(part3))))


def get_priority(triplet):
    return get_priority_char(get_common_item(triplet[0], triplet[1], triplet[2]))

priorities = []
for i in range(0, len(rows), 3):
    triple = rows[i:i+3:]
    priorities.append(get_priority(triple))

print(sum(priorities))
