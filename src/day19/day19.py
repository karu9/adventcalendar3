import sys
maze = list(map(lambda x : [x[i] for i in range(len(x))], [y[:-1] for y in open('input.txt').readlines()]))
sys.setrecursionlimit(len(maze)*len(maze[0]))
mazeStart = (0, maze[0].index('|'))
def parcourt(start, direction, word, steps):
    currPos = (start[0] + direction[0], start[1] + direction[1])
    currVal = maze[currPos[0]][currPos[1]]
    steps[0] += 1
    while currVal != ' ' and  currVal != '+':
        if currVal in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            word.append(currVal)
        currPos = (currPos[0] + direction[0], currPos[1] + direction[1])
        currVal = maze[currPos[0]][currPos[1]]
        steps[0] += 1
    if currVal == ' ':
        return
    elif currVal == '+':
        previousVal = maze[start[0]][start[1]]
        possibleValues = [(currPos[0] + direction[1], currPos[1] + direction[0]), (currPos[0] - direction[1], currPos[1] - direction[0])]
        nextPos = list(filter(lambda x : x[0] in range(len(maze)) and x[1] in range(len(maze[0])) and maze[x[0]][x[1]] == ('|' if previousVal == '-' else '-'), possibleValues))[0]
        parcourt(nextPos, (nextPos[0] - currPos[0], nextPos[1] - currPos[1]), word, steps)
        steps[0] += 1
finalword = []
finalsteps = [0]
parcourt(mazeStart, (1, 0), finalword, finalsteps)
print(''.join(finalword), finalsteps[0])
