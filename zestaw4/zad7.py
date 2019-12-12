def flatten(sequence):
    L = list()
    for item in sequence:
        if isinstance(item, (list,tuple)):
            L += flatten(item)
        else:
            L.append(item)
    return L


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(seq)
print(flatten(seq))










