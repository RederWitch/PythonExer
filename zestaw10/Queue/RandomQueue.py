from random import randint as ran

class RandomQueue:

    def __init__(self, size=6):
        if size <= 0:
            raise ValueError("zły rozmiar kolejki")
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne

    def insert(self, item):
        if self.is_full():
            raise IndexError("Pełna Kolejka")
        else:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.n

    def remove(self):   # zwraca losowy element
        if self.is_empty():
            raise IndexError("Z pustego i Salomon nie naleje")
        else:
            x = ran(self.head, self.tail-1)
            item = self.items[x]
            self.items[x] = self.items[self.head]
            self.items[self.head] = None
            self.head = (self.head + 1) % self.n
            return item

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def clear(self):    # czyszczenie listy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne



