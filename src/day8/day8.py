## part 1 ##
lines = open('input.txt').readlines()
## 0 = register 1 = action 2 = amount 4 = left condition 5 = comparison 6 = right condition
operations = list(map(lambda x : x[:-1].split(' '), lines))
registers = []
def condition(op):
    register = list(filter(lambda x : x[0] == op[4], registers))
    if len(register) == 0:
        register = [[op[4], 0]]
        registers.append(register[0])
    comparison = op[5]
    value = int(op[6])
    if comparison == '>':
        return register[0][1] > value
    if comparison == '>=':
        return register[0][1] >= value
    if comparison == '<':
        return register[0][1] < value
    if comparison == '<=':
        return register[0][1] <= value
    if comparison == '==':
        return register[0][1] == value
    if comparison == '!=':
        return register[0][1] != value

def action(op):
    register = list(filter(lambda x : x[0] == op[0], registers))
    if len(register) == 0:
        register = [[op[0], 0]]
        registers.append(register[0])
    action = op[1]
    value = int(op[2])
    if action == 'inc':
        register[0][1] += value
    else:
        register[0][1] -= value
maxRegister = 0
for op in operations:
    if condition(op):
        action(op)
    maxRegister = max(maxRegister, max(list(map(lambda x : x[1], registers))))
print(max(list(map(lambda x : x[1], registers))))
print(maxRegister)
