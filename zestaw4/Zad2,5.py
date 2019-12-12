#Z powodu nie wiedzy czy wymagane jest by funkcje przyjmowały
# jakieś zmienne postanowiłam wykonać drugą wersję zadania

def ruler( size ):
    line1 = "|"
    line2 = "0"
    n = 0
    while n < size:
        line1 = line1 + "....|"
        n = n + 1
        if n < 10:
            line2 = line2 + 4 * " " + str(n)
        else:
            line2 = line2 + 3 * " " + str(n)
    result = line1 + "\n" + line2
    return (result)

def net( wight, hight):
    line1 = ""
    line2 = ""
    n = 0

    while n < wight:
        if n == 0:
            line1 = "+"
            line2 = "|"
        line1 = line1 + "---+"
        line2 = line2 + "\t|"
        n += 1

    n = 1
    result = line1
    while n <= hight:
        result = result + "\n" + line2 + "\n" + line1
        n += 1
    return result


print("Zad 3.5 ruler:")
while True :
    inSize = input("Podaj wielkość miarki: ")
    try:
        size = int(inSize)
    except ValueError:
        print("To nie liczba, jeszcze raz")
        continue
    else:
        if size < 0 :
            print("Zły rozmiar, spróbuj jeszcze raz")
            continue
        else: break
print(ruler(size))

print("Zad 3.6 net:")
while True:
    hight = input("Podaj wysokość siatki: ")
    try:
        hight = int(hight)
    except ValueError:
        print("To nie liczba, spróbuj jeszcze raz")
        continue
    else:
        if hight < 0:
            print("Wysokość < 0, spróbuj jeszcz raz")
            continue
        else:
            break

while True:
    wight = input("Podaj szerokość siatki: ")
    try:
        wight = int(wight)
    except ValueError:
        print("To nie liczba, spróbuj jeszcze raz")
        continue
    else:
        if wight <0:
            print("Szerokosc < 0, spróbuj jeszcz raz")
            continue
        else:
            break
print(net(wight, hight))
