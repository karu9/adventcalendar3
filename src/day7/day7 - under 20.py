values = list(map (lambda x : [x[0:x.index(' ')], x[x.index('(')+1: x.index(')')], [] if '>' not in x else x[x.index('>') + 1 : -1].strip().split(', ')], open('input.txt').readlines()))
root = list(filter(lambda x : x[0] not in sum(list(map(lambda y : y[2], values)), []), values))[0]
## part 1 ##
print(root)
## part 2 ##
def findWeight(diskName):
    disk = list(filter(lambda x : x[0] == diskName, values))[0]
    weights = list(map(lambda x : int(findWeight(x)), disk[2]))
    if len(set(weights)) == 2:
        print(weights)
        print(list(map(lambda x: list(filter(lambda y : y[0] == x, values))[0][1], disk[2])))
    return sum(weights) + int(disk[1])
findWeight(root[0])
