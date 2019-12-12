
def odwracanie(L, left, right):
    L[left:right+1] = L[left:right+1][::-1]
    return L



L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(L)
print(odwracanie(L, 3, 6))
