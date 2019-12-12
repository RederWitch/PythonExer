def odwracanie(L, left, right):
    if left == right:
        return
    else:
        tem = L[right]
        del L[right]
        L[left:left] = [tem]
        odwracanie(L, left+1, right)


L = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(L)
odwracanie(L,3,6)
print(L)