rules = [[x[0: x.index(' =>')].split('/'), x[x.index('>')+ 2 : -1].split('/')] for x in open('input.txt').readlines()]
my_grid = ['##..', '..#.', '#.#.', '....']
def transform_grid(sub_grid):
    for rule in rules:
        rule_condition = sorted([sorted(x) for x in rule[0]])
        if len(rule_condition) == len(sub_grid):
            sorted_sub_grid = sorted([sorted(x) for x in sub_grid])
            if sorted_sub_grid == rule_condition:
                return rule[1]
def regroup_grids(sub_grids):
    print(sub_grids[1])
    grid = []
    for x in range(len(sub_grids)):
        sub_grid = []
        for y in range(len(sub_grids)):
            print(sub_grids[y][x]) 
        grid.append(sub_grid)
    return grid
def get_transformed_grid(grid):
    slice_len = 2 if len(grid) % 2 == 0 else 3
    number_of_grids = int(len(grid) / slice_len)
    sub_grids = []
    for x in range(number_of_grids):
        sub_grid = []
        for y in range(number_of_grids):
            sub_grid.append(transform_grid([grid[z][x * slice_len: x * slice_len + slice_len] for z in range(y, y + slice_len)]))
        sub_grids.append(sub_grid)
    return regroup_grids(sub_grids)
print(get_transformed_grid(my_grid))
                                   
