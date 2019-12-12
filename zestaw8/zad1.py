

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    y = -c/b
    x = (-b*y -c)/a
    return [x, y]


print(solve1(3, 1, -1))
print(solve1(2, 2, -4))
print(solve1(7, 4, 2))

