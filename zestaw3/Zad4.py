#zad4
while True:
    inText = input("Podaj liczbe: ")
    if inText == 'stop' : break
    try:
        number = float(inText)
    except ValueError:
        print("To nie liczba, prosze spróbować ponownie")
        continue
    else :
        print("Podana liczba: {}\tJej sześcian: {}".format(number,number**3))