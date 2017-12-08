## 0 = register 1 = action 2 = amount 4 = left condition 5 = comparison 6 = right condition
registers = {}
def operate(op):
    registers[op[4]] = registers[op[4]] if op[4] in registers.keys() else 0
    if eval("%s %s %s" % (registers[op[4]], op[5], int(op[6]))):
        registers[op[0]] = registers[op[0]] if op[0] in registers.keys() else 0
        exec("%s %s %s" % ("registers[op[0]] = registers[op[0]] ", '+' if op[1] == 'inc' else '-', int(op[2])))
    return max(registers.values())
maxRegisters = list(map(lambda x : operate(x), list(map(lambda x : x[:-1].split(' '), open('input.txt').readlines()))))
print(maxRegisters[-1], max(maxRegisters))
