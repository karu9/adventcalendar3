rules = [[x[0: x.index(' =>')].split('/'), x[x.index('>')+ 2 : -1].split('/')] for x in open('input.txt').readlines()]
my_grid = ['.#.', '..#', '###']
def get_flips_and_rotations(rule):
    result = []
    result.append(rule)
    ## rotations ##
    len_rule = len(rule)
    result.append([''.join([result[-1][x][k] for x in range(0,len_rule)]) for k in range(len_rule-1,-1,-1)])
    result.append([''.join([result[-1][x][k] for x in range(0,len_rule)]) for k in range(len_rule-1,-1,-1)])
    result.append([''.join([result[-1][x][k] for x in range(0,len_rule)]) for k in range(len_rule-1,-1,-1)])
    ## flips ##
    result.append(rule[::-1])
    result.append([''.join([result[-1][x][k] for x in range(0,len_rule)]) for k in range(len_rule-1,-1,-1)])
    result.append([''.join([result[-1][x][k] for x in range(0,len_rule)]) for k in range(len_rule-1,-1,-1)])
    result.append([''.join([result[-1][x][k] for x in range(0,len_rule)]) for k in range(len_rule-1,-1,-1)])
    return result
def transform_grid(sub_grid):
    matching_rules = []
    for rule in rules:
        rule_root = rule[0]
        if len(rule_root[0]) == len(sub_grid) and ''.join(rule_root).count('#') == ''.join(sub_grid).count('#'):
            rule_flipped_rotated = ['/'.join(x) for x in get_flips_and_rotations(rule_root)]
            if '/'.join(sub_grid) in rule_flipped_rotated:
                matching_rules.append(rule[1])
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
for i in range(18):
    my_grid = get_transformed_grid(my_grid)
    print(''.join(my_grid).count('#'))
