GRID = [x[:-1] for x in open('input.txt').readlines()]
CARRIER = [int(len(GRID[0])/2), int(len(GRID)/2)]
DIR = [0, -1]
counter = 0
def turn(is_left):
    if DIR[0] == 0 and DIR[1] == 1:
        if is_left:
            DIR = [1, 0]
        else:
            DIR = [-1, 0]
    elif DIR[0] == 0 and DIR[1] == -1:
        if not is_left:
            DIR = [1, 0]
        else:
            DIR = [-1, 0]
    elif DIR[0] == 1 and DIR[1] == 0:
        if is_left:
            DIR = [0, -1]
        else:
            DIR = [0, 1]
    else :
        if not is_left:
            DIR = [0, -1]
        else:
            DIR = [0, 1]
    CARRIER[0] += DIR[0]
    CARRIER[1] += DIR[1]
    if CARRIER[0] < 0 :
        CARRIER[0] = 0
        GRID = ['.' + x for x in GRID]
    if CARRIER[0] == len(GRID[0]):
        GRID = [x + '.' for x in GRID]


if __name__ == '__main__':
    for i in range(10000):
        print(len(GRID))
        if GRID[CARRIER[1]][CARRIER[0]] == '#':
            to_update = list(GRID[CARRIER[1]])
            to_update[CARRIER[0]] = '.'
            GRID[CARRIER[1]] = ''.join(to_update)
            turn(True)
        else :
            to_update = list(GRID[CARRIER[1]])
            to_update[CARRIER[0]] = '#'
            GRID[CARRIER[1]] = ''.join(to_update)
            counter += 1
            turn(False)
        print(counter)
