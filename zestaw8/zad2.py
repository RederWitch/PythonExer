from math import sqrt


def solve2(a, b, c):
    """Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
    if a == 0:
        print("Wynik X = {}".format(-c/b))
    else:
        delta = b**2 - 4 * a *c
        if delta < 0:
            print("Brak wyników")
        elif delta == 0:
            print("Wynik X = {}".format( -b/(2*a)))
        else:
            print("Wyniki X1 = {},\tX2 = {}".format((-b+sqrt(delta))/2*a, (-b-sqrt(delta))/2*a))
    return


"""
# a==0
solve1(0, 2, 5)
# delta < 0
solve1(2, 2, 1)
# delta == 0
solve1(1, 2, 1)
# delta > 0
solve1(1, 2, -3)
"""