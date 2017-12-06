import time
## part 1 ##
def mancala():
    maxValue = max(values)
    maxIndex = values.index(maxValue)
    values[maxIndex] = 0
    while maxValue != 0:
        maxIndex += 1
        maxValue -= 1
        values[maxIndex % len(values)] += 1
    return str(values)

starttime = time.time()
values = list(map(lambda x : int(x), open('input.txt').readlines()[0].split('\t')))
stringValues = str(values)
visitedStates = []
steps = 0
# part 1 #
while stringValues not in visitedStates:
    visitedStates.append(stringValues)
    stringValues = mancala()
    steps += 1
print(steps)
print(time.time() - starttime)
# part 2 #
loopingState = values.copy()
mancala()
steps = 1
while values != loopingState:
    mancala()
    steps += 1
print(steps)
print(time.time() - starttime)
