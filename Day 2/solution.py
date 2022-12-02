with open('input.txt', 'r') as f:
    raw = f.read()
rows = raw.split('\n')


def transform_to_move(char):
    if char in 'AX':
        return 'ROCK'
    elif char in 'BY':
        return 'PAPER'
    else:
        return 'SCISSORS'


move_score_lookup = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}


def is_winning(challenge, response):
    if challenge == 'ROCK':
        return response == 'PAPER'
    elif challenge == 'PAPER':
        return response == 'SCISSORS'
    else:
        return response == 'ROCK'


def score_game(ply1, ply2):
    if ply1 == ply2:
        return move_score_lookup[ply2] + 3
    if is_winning(ply1, ply2):
        return 6 + move_score_lookup[ply2]
    else:
        return move_score_lookup[ply2]


def transform_entry_1(entry):
    [opponent, response] = entry.split(' ')
    opponent = transform_to_move(opponent)
    response = transform_to_move(response)
    return score_game(opponent, response)


outcome_lookup = {
    'X': 'LOSE',
    'Y': 'DRAW',
    'Z': 'WIN'
}

response_lookup = {
    'ROCK': ['PAPER', 'SCISSORS'],
    'PAPER': ['SCISSORS', 'ROCK'],
    'SCISSORS': ['ROCK', 'PAPER']
}


def get_response(challenge, outcome):
    outcome = outcome_lookup[outcome]
    if outcome == 'DRAW':
        return challenge
    return response_lookup[challenge][outcome == 'LOSE']


def transform_entry_2(entry):
    [opponent, outcome] = entry.split(' ')
    opponent = transform_to_move(opponent)
    response = get_response(opponent, outcome)
    return score_game(opponent, response)


print(sum(list(map(transform_entry_1, rows))))
print(sum(list(map(transform_entry_2, rows))))
