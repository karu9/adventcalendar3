inp = 368078
x = 1
y = 0
array = [[0 for i in range (0, 50)] for i in range (0, 50)]
array[0][0] = 1
array[1][0] = 1

def sumArray(x, y):
    arraySum = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            arraySum += array[x+i][y+j]
    return arraySum

def checkValue(x, y, inp):
    inp -= 1
    arraySum = sumArray(x, y);
    array[x][y] = arraySum
    if arraySum > inp:
        print(arraySum)
    if inp == 2:
        print(x, y)
        print(abs(x) + abs(y))

while True:
    while y < x:
        y += 1
        checkValue(x, y, inp)
    while x > -y:
        x -= 1
        checkValue(x, y, inp)
    while y > x:
        y -= 1
        checkValue(x, y, inp)
    while x <= -y:
        x += 1
        checkValue(x, y, inp)
    
