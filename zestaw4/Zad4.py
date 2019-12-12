def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fn = 0
    fn1 = 1
    i = 2
    while i < n:
        if i % 2 == 0:
            fn = fn + fn1
            i += 1
        else:
            fn1 = fn + fn1
            i += 1
    result = fn + fn1
    return result


n = int(input("Podaj n: "))
print("Wynik: {}".format(fibonacci(n)))