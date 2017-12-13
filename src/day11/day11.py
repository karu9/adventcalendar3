coords = [[0, 0]]
for instruction in open('input.txt').readlines()[0].split(',') :
    coords.append([x + y for x, y in zip(coords[-1], {'n':[0,1], 's':[0,-1], 'nw':[-0.5, 0.5], 'ne':[0.5,0.5], 'se':[0.5, -0.5], 'sw':[-0.5,-0.5]}[instruction])])
print(int(2*abs(coords[-1][0]) if abs(coords[-1][0]) > abs(coords[-1][1]) else abs(coords[-1][0]) + abs(coords[-1][1])))
print(max(list(map(lambda x : int(2*abs(x[0]) if abs(x[0]) > abs(x[1]) else abs(x[0]) + abs(x[1])), coords))))
