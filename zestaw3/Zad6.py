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

print("Wielość siatki {}X{}".format(hight, wight))

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
net = line1
while n <= hight:
    net = net +"\n" + line2 + "\n" + line1
    n += 1

print(net)

