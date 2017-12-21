rules = [[x[0: x.index(' =>')].split('/'), x[x.index('>')+ 2 : -1].split('/')] for x in open('input.txt').readlines()]
my_grid = ['.#.', '..#', '###']
def transform_grid(sub_grid):
    matching_rules = []
    for rule in rules:
        rule_condition = sorted([sorted(x) for x in rule[0]])
        if len(rule_condition) == len(sub_grid):
            sorted_sub_grid = sorted([sorted(x) for x in sub_grid])
            if sorted_sub_grid == rule_condition:
                matching_rules.append(rule[1])
    print(len(matching_rules))
    return matching_rules[0]
def regroup_grids(sub_grids):
    grid = []
    for row in range(len(sub_grids)):
        for subrow in range(len(sub_grids[0][0])):
            val = ''
            for column in range(len(sub_grids[0])):
                val += sub_grids[row][column][subrow]
            grid.append(val)
    return grid
def get_transformed_grid(grid):
    slice_len = 2 if len(grid) % 2 == 0 else 3
    number_of_grids = int(len(grid) / slice_len)
    sub_grids = []
    for x in range(number_of_grids):
        sub_grid = []
        for y in range(number_of_grids):
            sub_grid.append(transform_grid([grid[z][y * slice_len: y * slice_len + slice_len] for z in range(x * slice_len, x * slice_len + slice_len)]))
        sub_grids.append(sub_grid)
    return regroup_grids(sub_grids)
for i in range(5):
    my_grid = get_transformed_grid(my_grid)
    print(len(my_grid))
