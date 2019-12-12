from math import gcd


def add_frac(frac1, frac2):        # frac1 + frac2
    result = [0, 0]
    if frac1[1] == frac2[1]:
        result = [frac1[0]+frac2[0], frac1[1]]
        result = minimal_frac(result)
        return corect_form(result)
    elif is_zero(frac1):
        result = minimal_frac(frac2)
        return corect_form(result)
    elif is_zero(frac2):
        result = minimal_frac(frac1)
        return corect_form(result)
    else:
        result = [frac1[0]*frac2[1] + frac2[0]*frac1[1], frac1[1]*frac2[1]]
        result = minimal_frac(result)
        return corect_form(result)


def sub_frac(frac1, frac2):        # frac1 - frac2
    frac2[0] = -frac2[0]
    return add_frac(frac1, frac2)


def mul_frac(frac1, frac2):        # frac1 * frac2
    result = [0, 0]
    if frac1[0] == 0:
        return [0, 1]
    elif frac2[0] == 0:
        return [0, 1]
    else:
        result[0] = frac1[0]*frac2[0]
        result[1] = frac1[1] * frac2[1]
        result = minimal_frac(result)
        return corect_form(result)


def div_frac(frac1, frac2):         # frac1 / frac2
    if is_zero(frac2):
        return None
    else:
        temp = [frac2[1], frac2[0]]
        result = mul_frac(frac1, temp)
        return result


def is_positive(frac):             # bool, czy dodatni
    if frac2float(frac) > 0:
        return True
    else:
        return False


def is_zero(frac):                 # bool, typu [0, x]
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    flo1 = frac2float(frac1)
    flo2 = frac2float(frac2)
    if flo1 == flo2:
        return 0
    elif flo1 > flo2:
        return 1
    else:
        return -1


def frac2float(frac):              # konwersja do float
    if is_zero(frac):
        return float(0)
    else:
        return frac[0]/frac[1]


def minimal_frac(frac):
    hcd = gcd(frac[0], frac[1])
    if hcd != 0:
        return [frac[0]/hcd, frac[1]/hcd]
    else:
        return frac


def corect_form(frac):
    if frac[1] < 0:
        frac[0] = -frac[0]
        frac[1] = -frac[1]
        return frac
    else:
        return frac

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)
f6 = [-3, 4]
g1 = [6,1]
g2 = [6,6]
g3 = [4,2]
g4 = [1, 2]
g5 = [-7,21]
#print(div_frac(f4, f1))
#print(is_positive(f6))
#print(minimal_frac(g1))
#print(minimal_frac(g2))
#print(minimal_frac(g3))
#print(minimal_frac(g4))
#print(minimal_frac(g5))


