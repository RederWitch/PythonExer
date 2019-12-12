seq1 = "krotki"
seq2 = "kropki"

set1 = set()
set2 = set()
for item in seq1:
    set1.add(item)
for item in seq2:
    set2.add(item)
#print(set1)
#print(set2)

set3 = set1&set2
print("A")
print("Zbiór potarzających się elementów:")
print(set3)

print("B")
print("Zbiór wszystkich elementów")
set4 = set1 | set2
print(set4)