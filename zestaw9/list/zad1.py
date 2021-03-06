from Node import *

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def printSL(self):
        """Iteracyjne wypisanie listy jednokierunkowej."""
        if self.is_empty():
            print("Lista jest pusta")
        node = self.head
        while node:
            print(node)
            node = node.next

# start of my coding

    def merge(self, other):
        ''' Węzły z listy other są przepinane do listy self na jej koniec.'''
        node = other.head
        while node:
            self.insert_tail(node)
            self.length +=1
            node = node.next

    def clear(self):
        '''czyszczenie listy, usuwa powiazania head i tail oraz ustawia długosć na 0'''
        self.head = self.tail = None
        self.length = 0


    def remove_tail(self):
        ''' Zwraca cały węzeł, skraca listę.
            Dla pustej listy rzuca wyjątek ValueError.
            klasy O(N) '''
        if self.is_empty():
            raise ValueError
        node = self.head
        if node.next == None:
            self.length -= 1
            self.head = None
            return node
        node_next = node.next
        while node_next.next:
            node = node_next
            node_next = node_next.next
        self.length -= 1
        node.next = None
        return node_next
