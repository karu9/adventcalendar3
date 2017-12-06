## part 1 ##
values = list(map(lambda x : int(x), open('input.txt').readlines()[0].split('\t')))
visitedStates = []
steps = 0
def mancala():
    maxValue = max(values)
    maxIndex = values.index(maxValue)
    values[maxIndex] = 0
    while maxValue != 0:
        maxIndex += 1
        maxValue -= 1
        values[maxIndex % len(values)] += 1
# part 1 #
while values not in visitedStates:
    visitedStates.append(values.copy())
    mancala()
    steps += 1
print(steps)
# part 2 #
visitedStates = visitedStates[-1:]
steps = 1
while values not in visitedStates:
    visitedStates.append(values.copy())
    mancala()
    steps += 1
print(steps)
    
