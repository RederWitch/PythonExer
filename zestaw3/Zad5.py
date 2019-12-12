while True:
    inSize = input("Podaj wielkość miarki: ")
    try:
        size = int(inSize)
    except ValueError:
        print("To nie liczba, jeszcze raz")
        continue
    else:
        if size < 0:
            print("Zły rozmiar, spróbuj jeszcze raz")
            continue
        else:
            break

line1 = "|"
line2 = "0"
n = 0
while n < size:
    line1 = line1 + "....|"
    n = n+1
    if n<10:
        line2 = line2 + 4*" " + str(n)
    else:
        line2 = line2 + 3*" " + str(n)
ruler = line1 + "\n" + line2
print(ruler)
