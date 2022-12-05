with open('input.txt', 'r') as f:
    raw = f.read()
rows = raw.split('\n')

# skip stack definition
rows = rows[10::]

stack1 = 'JHPMSFNV'
stack2 = 'SRLMJDQ'
stack3 = 'NQDHCSWB'
stack4 = 'RSCL'
stack5 = 'MVTPFB'
stack6 = 'TRQNC'
stack7 = 'GVR'
stack8 = 'CZSPDLR'
stack9 = 'DSJVGPBF'

stacks = list(map(lambda x: list(x), [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]))


class Move(object):
    def __init__(self, source, target, depth):
        self.source_index = source - 1
        self.target_index = target - 1
        self.depth = depth

    def apply(self, stcks):
        src = stcks[self.source_index]
        targ = stcks[self.target_index]
        to_move = src[len(src) - self.depth:len(src)]
        assert (len(to_move) == self.depth)
        for i in to_move[::-1]:
            targ.append(i)
        stcks[self.source_index] = src[:len(src) - self.depth:]

    def __str__(self):
        return '[' + str(self.source_index + 1) + ' -> ' + str(self.target_index + 1) + '; ' + str(self.depth) + ']'


def create_move(row: str):
    row = row.split(' ')
    return Move(int(row[3]), int(row[5]), int(row[1]))


moves = list(map(create_move, rows))
print(len(moves))

n_before = sum(list(map(lambda x: len(x), stacks)))

for move in moves:
    move.apply(stacks)

n_after = sum(list(map(lambda x: len(x), stacks)))

assert (n_after == n_before)

for i in range(len(stacks)):
    print("stack ", i + 1, ": ", str(stacks[i]))


def get_top(stack):
    if len(stack) == 0:
        return ' '
    return stack[-1]


print(list(map(get_top, stacks)))
print('[', ''.join(list(map(get_top, stacks))), ']')
