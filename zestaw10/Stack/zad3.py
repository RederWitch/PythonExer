class Stack:

    def __init__(self):
        self.items = []
        self.dictionary = {}

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pełny
        return False

    def push(self, item):
        if self.is_full():
            raise ValueError("Pełen Stos")
        if item in self.dictionary and self.dictionary[item] == 1:
            pass
        else:
            self.dictionary[item] = 1
            self.items.append(item)

    def pop(self):                      # zwraca element
        if(self.is_empty()):
            raise ValueError("Pusty Stos")
        item = self.items.pop()
        self.dictionary[item] = 0
        return item         # zabieram od końca

