grid = [x[:-1] for x in open('input.txt').readlines()]
carrier = [int(len(grid[0])/2), int(len(grid)/2)]
direction = [0, -1]
counter = [0]
def turn(is_left, direction):
    if direction[0] == 0 and direction[1] == 1:
        if is_left:
            direction = [1, 0]
        else:
            direction = [-1, 0]
    elif direction[0] == 0 and direction[1] == -1:
        if not is_left:
            direction = [1, 0]
        else:
            direction = [-1, 0]
    elif direction[0] == 1 and direction[1] == 0:
        if is_left:
            direction = [0, -1]
        else:
            direction = [0, 1]
    else :
        if not is_left:
            direction = [0, -1]
        else:
            direction = [0, 1]
    carrier[0] += direction[0]
    carrier[1] += direction[1]
    if carrier[0] < 0 :
        carrier[0] = 0
        grid = ['.' + x for x in grid]
    if carrier[0] == len(grid[0]):
        grid = [x + '.' for x in grid]
    return direction
for i in range(10000):
    if grid[carrier[1]][carrier[0]] == '#':
        to_update = list(grid[carrier[1]])
        to_update[carrier[0]] = '.'
        grid[carrier[1]] = ''.join(to_update)
        direction = turn(True, direction)
    else :
        to_update = list(grid[carrier[1]])
        to_update[carrier[0]] = '#'
        grid[carrier[1]] = ''.join(to_update)
        counter[0] += 1
        direction = turn(False, direction)
print(counter[0])
