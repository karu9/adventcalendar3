## crap from d10-2 ##
def knothash(word) :
    elements = [x for x in range(256)]
    lenghts = list(map(lambda x : ord(x), word)) + [17, 31, 73, 47, 23]
    index = 0
    skip_size = 0
    for h in range(64):
        for inp in lenghts:
            reversedList = (elements + elements)[index:index + int(inp)][::-1]
            for i in range(len(reversedList)):
                elements[(index + i) % len(elements)] = reversedList[i]
            index = (index + int(inp) + skip_size) % len(elements)
            skip_size += 1
    denseHash = []
    for i in range(16) :
        xor = elements[16*i]
        for element in elements[16*i + 1 : 16*i + 16]:
            xor ^= element
        denseHash.append(('0' +hex(xor)[2:])[-2:])
    return(''.join(denseHash))
## end crap from d10-2 ##
## part 1 ##
knothashes = [knothash('nbysizxe-' + str(y)) for y in range(128)]
weights = {'0' : 0, '1' : 1, '2' : 1, '3' : 2, '4' : 1, '5': 2, '6': 2, '7' : 3, '8' : 1, '9' : 2, 'a':  2, 'b' : 3, 'c' : 2, 'd' : 3, 'e' : 3, 'f' : 4}
print(sum(list(map(lambda x : weights[x], ''.join(knothashes)))))
## part 2 ##
mapping = {'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5': '0101', '6': '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'a':  '1010', 'b' : '1011', 'c' : '1100', 'd' : '1101', 'e' : '1110', 'f' : '1111'}
grid = list(map(lambda x : ''.join([mapping[j] for j in x]), knothashes))
clusters = []
def findadjacent (x, y, cluster):
    ## if we are out of boundaries do nothing ##
    if not x in range(128) or not y in range(128):
        return
    ## if not used, do nothing ##
    if grid[y][x] == '0' :
        return
    ## if already in group, do nothing ##
    if len(list(filter(lambda c : [x,y] in c, clusters))) != 0 or [x,y] in cluster:
        return
    ## found a new group, youhouu ##
    cluster.append([x,y])
    findadjacent(x+1, y, cluster)
    findadjacent(x-1, y, cluster)
    findadjacent(x, y+1, cluster)
    findadjacent(x, y-1, cluster)
for i in range(128):
    for j in range(128):
        cluster = []
        findadjacent(i, j, cluster)
        if len(cluster) > 0:
            clusters.append(cluster)
print(len(clusters))
    
