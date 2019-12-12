from math import sqrt

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    T = [a, b, c]
    max_side = max(T)
    T.remove(max_side)
    if (T[0] + T[1]) <= max_side:
        raise ValueError("Nie spełniono warunku trójkąta")
    else:
        p = (a+b+c)/2
        return sqrt(p*(p-a)*(p-b)*(p-c))


