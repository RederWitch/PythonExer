from zestaw9.zad1 import *
print("SL")
SL = SingleList()
SL.printSL()
SL.insert_head(Node(2))
SL.insert_head(Node(4))
SL.insert_tail(Node(3))
#SL = 4 2 3
SL.printSL()
print()
print("OL")
OL = SingleList()
OL.insert_head(Node(777))
OL.printSL()
print()
print("merge")
PL = SingleList()
SL.merge(OL)
SL.printSL()
print()
print("SL tail")
print(SL.remove_tail())
print("SL bez tail")
SL.printSL()
print("OL tail")
print(OL.remove_tail())
print("OL bez tail")
OL.printSL()
print()
print("SL tail")
print(SL.remove_tail())
print("SL bez tail")
SL.printSL()
