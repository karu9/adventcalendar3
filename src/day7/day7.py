## part 1 ##
lines = open('input.txt').readlines()
values = []
for line in lines:
    value = [line[0:line.index(' ')], line[line.index('(')+1: line.index(')')], []]
    if '>' in line:
        value[2] = line[line.index('>') + 1 : -1].strip().split(', ')
    values.append(value)
## part 1 ##
root = values[0]
for value in values:
    contained = False
    if len(value[2]) > 0:
        for value2 in values:
            if value[0] in value2[2]:
                contained = True
                break
    else :
        continue
    if not contained:
        root = value
        break
print(root)
def getdisk(name):
    for value in values:
        if value[0] == name :
            return value
def findWeight(diskName):
    disk = getdisk(diskName)
    if len(disk[2]) == 0:
        return int(disk[1])
    weights = list(map(lambda x : int(findWeight(x)), disk[2]))
    setWeights = set(weights)
    if len(setWeights) != 1:
        print(weights)
        print(list(map(lambda x: getdisk(x)[1], disk[2])))
    return sum(weights) + int(disk[1])
findWeight(root[0])
