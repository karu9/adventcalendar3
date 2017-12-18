instructs = [x[:-1].split(' ') for x in open('input.txt').readlines()]
def initreg(instructs, registers):
    for instruct in instructs: 
        if not instruct[1].replace('-', '').isdigit() and instruct[1] not in registers:
            registers[instruct[1]] = 0
    return registers
def getintval(val, registers):
    intval = 0
    if not val.replace('-', '').isdigit():
        intval = registers[val]
    else:
        intval = int(val)
    return intval
def set(reg, val, registers, values):
    registers[reg] = getintval(val, registers)
    values[0] += 1
def mul(reg, val, registers, values):
    registers[reg] *= getintval(val, registers)
    values[0] += 1
def jgz(reg, val, registers, values):
    if getintval(reg, registers) > 0:
        values[0] += getintval(val, registers)
    else :    
        values[0] += 1
def add(reg, val, registers, values):
    registers[reg] += getintval(val, registers)
    values[0] += 1
def mod(reg, val, registers, values):
    registers[reg] %= getintval(val, registers)
    values[0] += 1
def snd(reg, registers, values, othersvalues, myqueue, othersqueue):
    othersqueue.append(getintval(reg, registers))
    othersvalues[1] = True
    values[2] += 1
    values[0] += 1
def rcv(reg, registers, values, othersvalues, myqueue, othersqueue):
    if len(myqueue) > 0:
        registers[reg] = myqueue.pop(0)
        values[0] += 1
    else :
        values[1] = False
def apply(instruct, registers, myval, othersval, myqueue, othersqueue):
    if instruct[0] == 'set':
        set(instruct[1], instruct[2], registers, myval)
    elif instruct[0] == 'mul':
        mul(instruct[1], instruct[2], registers, myval)
    elif instruct[0] == 'jgz':
        jgz(instruct[1], instruct[2], registers, myval)
    elif instruct[0] == 'add':
        add(instruct[1], instruct[2], registers, myval)
    elif instruct[0] == 'mod':
        mod(instruct[1], instruct[2], registers, myval)
    elif instruct[0] == 'snd':
        snd(instruct[1], registers, myval, othersval, myqueue, othersqueue)
    elif instruct[0] == 'rcv':
        rcv(instruct[1], registers, myval, othersval, myqueue, othersqueue)
def generate ():
    vals1 = [0, True, 0]
    vals2 = [0, True, 0]
    registers1 = initreg(instructs, {'p': 0})
    registers2 = initreg(instructs, {'p': 1})
    queue1 = []
    queue2 = []
    while vals1[1] or vals2[1]:
        if vals1[1]:
            instruct = instructs[vals1[0]]
            apply(instruct, registers1, vals1, vals2, queue1, queue2)
        if vals2[1]:
            instruct = instructs[vals2[0]]
            apply(instruct, registers2, vals2, vals1, queue2, queue1)
    print(vals1, vals2)
generate()

