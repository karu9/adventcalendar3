my_grid = [x[:-1] for x in open('input.txt').readlines()]
my_carrier = [int(len(my_grid[0])/2), int(len(my_grid)/2)]
my_direction = [0, -1]
counter = 0
def turn(is_left, carrier, direction, grid):
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
    if carrier[1] < 0 :
        carrier[1] = 0
        grid = [['.' for x in range(len(grid[0]))]] + grid
    if carrier[1] == len(grid):
        grid.append(['.' for x in range(len(grid[0]))])
    return [carrier, direction, grid]
for i in range(10000):
    if my_grid[my_carrier[1]][my_carrier[0]] == '#':
        to_update = list(my_grid[my_carrier[1]])
        to_update[my_carrier[0]] = '.'
        my_grid[my_carrier[1]] = ''.join(to_update)
        res = turn(False, my_carrier, my_direction, my_grid)
        my_carrier = res[0]
        my_direction = res[1]
        my_grid = res[2]
    else :
        to_update = list(my_grid[my_carrier[1]])
        to_update[my_carrier[0]] = '#'
        my_grid[my_carrier[1]] = ''.join(to_update)
        counter += 1
        res = turn(True, my_carrier, my_direction, my_grid)
        my_carrier = res[0]
        my_direction = res[1]
        my_grid = res[2]
print(counter)
