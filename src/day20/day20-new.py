import math
particules = [[[int(z) for z in y[0][3:-1].split(',')], [int(z) for z in y[1][3:-1].split(',')], [int(z) for z in y[2][3:-1].split(',')]] for y in [x[:-1].split(', ') for x in open('input.txt').readlines()]]
def calc_dis (particule, index):
    return sum(list(map(lambda x : abs(particule[0][x] + particule[1][x] * index + 0.5 * particule[2][x]* index * index), range(3))))
dists = list(map(lambda x : calc_dis(x, 100000000000),  particules))
print(dists.index(min(dists)))
## part 2 ##
def calc_pos(partic1, index):
    p = [x for x in partic1[0]]
    v = [x for x in partic1[1]]
    a = [x for x in partic1[2]]
    for i in range(index):
        for j in range(3):
            v[j] += a[j]
            p[j] += v[j]
    return p
def get_dist(p1, p2):
    return sum(list(map(lambda x : abs(p1[x] - p2[x]), range(3))))
def filter_colisions(partics):
    colisions = []
    result = [x for x in partics]
    for i in range(len(partics)):
        for j in range(i+1, len(partics)):
            part1 = partics[i]
            part2 = partics[j]
            ind = 0
            pos1 = calc_pos(part1, ind)
            pos2 = calc_pos(part2, ind)
            dist = get_dist(pos1, pos2)
            if dist == 0:
                colisions.append([0, pos1, pos2])
            else:
                ind += 1
                nextpos1 = calc_pos(part1, ind)
                nextpos2 = calc_pos(part2, ind)
                nexposdist = get_dist(nextpos1, nextpos2)
                while  nexposdist != 0 and nexposdist < dist :
                    pos1 = nextpos1
                    pos2 = nextpos2
                    dist = nexposdist
                    ind += 1
                    nextpos1 = calc_pos(part1, ind)
                    nextpos2 = calc_pos(part2, ind)
                    nexposdist = get_dist(nextpos1, nextpos2)
                if nexposdist == 0:
                    this_colision = [ind, part1, part2]
                    colisions.append(this_colision)
                    for colision in [x for x in colisions] :
                        if part1 in colision or part2 in colision :
                            if colision[0] > ind:
                                colisions.remove(colision)
                            elif  ind > colision[0]:
                                colisions.remove(this_colision)
    for colision in colisions:
        if colision[1] in result:
            result.remove(colision[1])
        if colision[2] in result:
            result.remove(colision[2])
    return result
print(len(filter_colisions(particules)))
