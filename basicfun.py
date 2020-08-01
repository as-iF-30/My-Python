import itertools
l = [1,3,2,6,1,2]
c = 0
t = list(itertools.combinations(l,2))
print(t)
l = [1,2,3]
t = list(itertools.permutations(l))
print(t)
