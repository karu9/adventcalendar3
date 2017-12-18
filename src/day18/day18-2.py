instructs = [x[:-1].split(' ') for x in open('input.txt').readlines()]
def initreg(reg, registers):
    if reg not in registers:
        registers[reg] = 0
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
    if registers[reg] > 0:
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
def generate ():
    vals1 = [0, True, 0]
    vals2 = [0, True, 0]
    registers1 = {'p': 0}
    registers2 = {'p': 1}
    queue1 = []
    queue2 = []
    while vals1[1] or vals2[1]:
        if vals1[1]:
            instruct = instructs[vals1[0]]
            initreg(instruct[1], registers1)
            exec(instruct[0] + '("' + instruct[1] + '","' + instruct[2] + '", registers1, vals1)' if len(instruct) == 3 else instruct[0] + '("' + instruct[1] + '", registers1, vals1, vals2, queue1, queue2)')
        if vals2[1]:
            instruct = instructs[vals2[0]]
            initreg(instruct[1], registers2)
            exec(instruct[0] + '("' + instruct[1] + '","' + instruct[2] + '", registers2, vals2)' if len(instruct) == 3 else instruct[0] + '("' + instruct[1] + '", registers2, vals2, vals1, queue2, queue1)')
    print(vals1, vals2)
generate()

