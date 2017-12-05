inp = 368078
x = 1
y = 0
while True:
    while y < x:
      y += 1
      inp -= 1
      if inp == 0:
          print(x, y)
    while x > -y:
      x -= 1
      inp -= 1
      if inp == 0:
          print(x, y)
    while y > -x:
      y -= 1
      inp -= 1
      if inp == 0:
          print(x, y)
    while x <= y:
      x += 1
      inp -= 1
      if inp == 0:
          print(x, y)
    
