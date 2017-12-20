import math
particules = [[y[0][3:-1].split(','),y[1][3:-1].split(','), y[2][3:-1].split(',')] for y in [x[:-1].split(', ') for x in open('input.txt').readlines()]]
def calc_dis (particule, index):
    return sum(list(map(lambda x : abs(int(particule[0][x]) + int(particule[1][x]) * index + 0.5 * int(particule[2][x])* index * index), range(3))))
dists = list(map(lambda x : calc_dis(x, 100000000000),  particules))
print(dists.index(min(dists)))
## part 2 ##
def get_pos(particule, coord, index):
    return int(particule[0][coord]) + int(particule[1][coord]) + int(particule[2][coord]) * index
def get_sols(p, v, a):
    if a == 0:
        if v == 0:
            if p == 0:
                return [0.0]
            else :
                return []
        else :
            if p == 0:
                return [0.5]
            else :
                return [-p/v]
    else:
        if p == 0:
            return [0.0, -2*v/a]
        discr = v * v - 2 * p * a
        if discr < 0:
            return []
        return [(-v - math.sqrt(discr))/ (2 * p), (-v + math.sqrt(discr))/ (2 * p)]
        
def get_colide_index (partic1, partic2):
    p = list(map(lambda x : int(partic1[0][x]) - int(partic2[0][x]), range(3)))
    v = list(map(lambda x : int(partic1[1][x]) - int(partic2[1][x]), range(3)))
    a = list(map(lambda x : int(partic1[2][x]) - int(partic2[2][x]), range(3)))
    sols = [get_sols(p[x], v[x], a[x]) for x in range(3)]
    for x in sols[0]:
        if x >=0 and x.is_integer() :
           for y in sols[1] :
               if y == x :
                   for z in sols[2]:
                       if z == x:
                           print(p, v, a)
                           print(sols)
                           return z
    return 0.5
def filter_colisions(partics):
    colisions = []
    for i in range(len(partics)):
        for j in range(i+1, len(partics)):
            colide_index = get_colide_index(partics[i], partics[j])
            if colide_index >= 0 and colide_index.is_integer():
                this_colision = [colide_index, partics[i], partics[j]]
                colisions.append(this_colision)
                for colision in [x for x in colisions] :
                    if colision == this_colision:
                        continue
                    if partics[i] in colision or partics[j] in colision:
                        if colision[0] < colide_index:
                            colisions.remove(this_colision)
                            break
                        elif colision[0] > colide_index :
                            colisions.remove(colision)
    print(colisions)
    result = [x for x in partics]
    for colision in colisions:
        if colision[1] in result:
            result.remove(colision[1])
        if colision[2] in result:
            result.remove(colision[2])
    return result
print(len(filter_colisions(particules)))
