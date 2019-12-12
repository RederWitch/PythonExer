# Zad 3
# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
n = 0
while n <= 30:
    if(n % 3) != 0:
        print(n)
    else:
        print("Podzielna przez 3")
    n += 1
del n

