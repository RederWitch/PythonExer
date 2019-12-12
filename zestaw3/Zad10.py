#Dla dopełnienia słownika dodałam rzymską liczbę 500 czyli D

D1 = {}
D1['I'] = 1
D1['V'] = 5
D1['X'] = 10
D1['L'] = 50
D1['C'] = 100
D1['D'] = 500
D1['M'] = 1000

# lub
D2 = dict()
D2['I'] = 1
D2['V'] = 5
D2['X'] = 10
D2['L'] = 50
D2['C'] = 100
D2['D'] = 500
D2['M'] = 1000


#inna metoda stworzenia takiego słownika
D3 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

D4 = dict([("I", 1), ("V", 5), ("X", 10), ('L', 50), ('C', 100), ("D", 500), ('M', 1000)])

D5 = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'],[1, 5, 10, 50, 100, 500, 1000]))

print("sposób 1: {}".format(D1.items()))
print("sposób 2: {}".format(D2.items()))
print("sposób 3: {}".format(D3.items()))
print("sposób 4: {}".format(D4.items()))
print("sposób 5: {}".format(D5.items()))

def roman2int(D, word):
    number = 0
    i = 0
    tem = 0

    while i<len(word):
        if i == len(word)-1:
            number += D[word[i]]
            i +=1
            continue
        if D[word[i]] < D[word[i+1]]:
            tem = D[word[i+1]] - D[word[i]]
            number += tem
            i += 2
            continue
        else:
            number += D[word[i]]
            i +=1
    del i
    del tem
    return number

print("\nDziałanie funkcji roman2int:")
print("Roman: MCMXLVI\t\t Int: {}".format(roman2int(D1, "MCMXLVI")))
print("Roman: MMMCDLXIX\t Int: {}".format(roman2int(D1, "MMMCDLXIX")))
