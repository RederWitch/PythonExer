from Node import*

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)
root.right.right.right = Node(9)


#        1
#      /   \
#    2       3
#   / \     / \
#  4   5   6   7

def btree_height(top):
    if top is None:
        return 0
    left = btree_height(top.left)
    right = btree_height(top.right)
    return 1 + max(left, right)


def btree_print_indented(top, level=0):
    if top is None:
        return
    btree_print_indented(top.right, level+1)
    print("{} * {}".format('     '*level, top.data))
    btree_print_indented(top.left, level+1)

#Zadanie 9.6
def count_total(top):
    """rekurencyjne zliczanie sumy danych w drzewie"""
    if top is None:
        return 0
    return count_total(top.left) + top.data + count_total(top.right)


def count_leaf(top):
    """rekurencyjne zliczanie lizby liści w drzewie"""
    leafcount = 0
    if top is None:
        return 0
    if (top.left is None) and (top.right is None):
        leafcount += 1
    return count_leaf(top.left) + leafcount + count_leaf(top.right)

print("Drzewo:")
btree_print_indented(root)
print("Suma liczb w drzewie:")
print(count_total(root))
print("Liczba liści w drzewie:")
print(count_leaf(root))
