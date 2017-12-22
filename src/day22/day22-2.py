my_grid = [x[:-1] for x in open('input.txt').readlines()]
my_carrier = [int(len(my_grid[0])/2), int(len(my_grid)/2)]
my_direction = [0, -1]
dictValue = {'.':'W', 'W':'#', '#':'F', 'F':'.'}
counter = 0
def turn(carrier, direction, grid, count):
    status = grid[carrier[1]][carrier[0]]
    if status in ['#', '.']:
        if direction[0] == 0 and direction[1] == 1:
            if status == '.':
                direction = [1, 0]
            else:
                direction = [-1, 0]
        elif direction[0] == 0 and direction[1] == -1:
            if status == '#':
                direction = [1, 0]
            else:
                direction = [-1, 0]
        elif direction[0] == 1 and direction[1] == 0:
            if status == '.':
                direction = [0, -1]
            else:
                direction = [0, 1]
        else :
            if status == '#':
                direction = [0, -1]
            else:
                direction = [0, 1]
    elif status == 'F':
        direction = [-direction[0], -direction[1]]
    to_update = list(grid[carrier[1]])
    if to_update[carrier[0]] == 'W':
        count += 1
    to_update[carrier[0]] =  dictValue[to_update[carrier[0]]]
    grid[carrier[1]] = ''.join(to_update)
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
    return [carrier, direction, grid, count]
for i in range(10000000):
    res = turn(my_carrier, my_direction, my_grid, counter)
    my_carrier = res[0]
    my_direction = res[1]
    my_grid = res[2]
    counter = res[3]
print(counter)
