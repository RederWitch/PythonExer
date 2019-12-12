from random import randrange
def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    r = 5
    counter = 0
    for i in range(n):
        x = randrange(r * 100 + 1)/100
        y = randrange(r * 100 + 1)/100
        if (x*x + y*y) <= r*r:
            counter += 1
    pi = counter/n
    return pi*4


def sr_pi(n):
    """Obliczanie średniej liczby pi z N razy obliczonej
     liczby pi metodą Monte Carlo"""
    L = []
    for i in range(n):
        L.append(calc_pi(1000))
    s = sum(L)
    pi = s/n
    return pi

"""
print(calc_pi(5))
print(calc_pi(25))
print(calc_pi(50))
print(calc_pi(75))
print(calc_pi())
print(calc_pi(1000))
print(calc_pi(1500))
print(calc_pi(2000))
print(calc_pi(10000))
print(calc_pi(15000))
print(calc_pi(20000))
"""
print(calc_pi(10000))
print("średnia ze {}: pi = {}".format(100, sr_pi(1000)))

