    #zad 10
    #Mamy dany napis wielowierszowy line.
    #Podać sposób obliczenia liczby wyrazów w napisie.
print("ZAD 10")
line = """ jeden    dwa
trzy cztery 
GvR
piec"""
lineSplit = line.split()
print("Liczba wyrazow: %d" % (len(lineSplit)))

    #zad 11
    #Podać sposób wyświetlania napisu word tak,
    # aby jego znaki były rozdzielone znakiem podkreślenia.
print("\nZAD 11")
S = "world"
print("_".join(S))

    #zad 12
    #Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.
    #Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
print("\nZAD 12")
S = ''
for item in lineSplit: S = S + item[0]
print("Napis z pierwszych liter: %s" % (S))
S = ''
for item in lineSplit: S = S + item[-1]
print("Napis z ostatnich liter: %s" % (S))

    #zad 13
    #Znaleźć łączną długość wyrazów w napisie line.

print("\nZAD 13")
X = 0
for item in lineSplit: X=X+len(item)
print("Dlugosc wyrazow: %d" % (X))

    # zad 14
    #Znaleźć: (a) najdłuższy wyraz,
    # (b) długość najdłuższego wyrazu w napisie line.
print("\nZAD 14")
lineDlugosc = sorted(lineSplit, key=len, reverse=True)
print("Najdluzszy wyraz: %s \nma dlugosc: %d"%(lineDlugosc[1], len(lineDlugosc[1])))

    #zad 15
    #Na liście L znajdują się liczby całkowite dodatnie.
    #Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
print("\nZAD 15")
L=[0,2,4,6,8,9]
S = ''
for item in L: S=S+str(item)
print("Lista: ")
print(L)
print("Słowo z listy: %s" % (S))

    #zad16
    #W tekście znajdującym się w zmiennej line zamienić
    #ciąg znaków "GvR" na "Guido van Rossum
print("\nZAD 16")
lineGvR = line.replace("GvR","Guido van Rossum")
print("\tline:")
print(line)
print("\n\tzmieniony line:")
print(lineGvR)

    #Zad17
    #Posortować wyrazy z napisu line
    # raz alfabetycznie,
    #a raz pod względem długości.
print("\nZAD 17")
print("Sortowanie alfabetycznie:")
print(sorted(lineSplit, key =str.lower))
print("Sortowanie względem długosci:")
print(sorted(lineSplit, key=len, reverse=True))

    #Zad18
    #Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.
    #Wskazówka: zamienić liczbę na napis.
print("\nZAD 18")
X = 99916020
Y = 79050740
Z = 60004000
X = str(X)
Y = str(Y)
Z = str(Z)
print("\tliczby\t\t:\tilosc 0")
print("\t%s\t:\t%d" % (X, X.count("0")))
print("\t%s\t:\t%d" % (Y, Y.count("0")))
print("\t%s\t:\t%d" % (Z, Z.count("0")))

    #Zad19
    #Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
    #Chcemy zbudować napis z trzycyfrowych bloków,
    #gdzie liczby jedno- i dwucyfrowe będą miały
    #blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
print("\nZAD 19")
L= [1, 22, 383, 4]
S =''
for item in L : S = S + str(item).zfill(3)
print("Lista L:")
print(L)
print("Napis z dopełnienim: %s" % (S))

