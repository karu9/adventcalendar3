particules = [[y[0][3:-1].split(','),y[1][3:-1].split(','), y[2][3:-1].split(',')] for y in [x[:-1].split(', ') for x in open('input.txt').readlines()]]
def calc_dis (particule, index):
    return sum(list(map(lambda x : abs(int(particule[0][x]) + int(particule[1][x]) + int(particule[2][x])*index), range(3))))
dists = list(map(lambda x : calc_dis(x, 100000000000),  particules))
print(dists.index(min(dists)))
## part 2 ##
def get_pos(particule, coord, index):
    return int(particule[0][coord]) + int(particule[1][coord]) + int(particule[2][coord])*index
def calc_colide(partics, index):
    to_remove = []
    for i in range(len(partics)):
        for j in range(i+1, len(partics)):
            part = partics[i]
            partic = partics[j]
            if get_pos(part, 0, index) == get_pos(partic, 0, index) and get_pos(part, 1, index) == get_pos(partic, 1, index) and get_pos(part, 2, index) == get_pos(partic, 2, index):
                to_remove.append(part)
                to_remove.append(partic)
    for part in to_remove:
        if part in partics:
            partics.remove(part)
for i in range(100):
    calc_colide(particules, i)
print(len(particules))
