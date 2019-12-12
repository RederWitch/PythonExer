L= [[1], [1,1], [1, 2],[1, 2, 1],[2, 3], [], [2,3,5]]
E = []
for item in L:
    E.append(sum([x for x in item]))

print(L)
print(E)

