clusters = []
for line in list(map(lambda x: [x[:x.index(" <->")]]+x[x.index('<-> ')+4:-1].split(', '), open('input.txt').readlines())) :
    matchingClusters = []
    for program in line :
        matchingClusters += list(filter(lambda x : program in x and x not in matchingClusters, clusters))
    for cluster in matchingClusters:
        clusters.remove(cluster)
    clusters.append(list(set(sum(matchingClusters, line))))
print(len(list(filter(lambda x : '0' in x, clusters))[0]), len(clusters))
