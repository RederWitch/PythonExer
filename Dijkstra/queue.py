from heapq import *

class QueueItem:
    def __init__(self, name, priority):
        self.name = name
        self._priority = priority
        self.queue = None

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority
        self.queue.rebuild_queue()

    def set_queue(self, queue):
        self.queue = queue

    def __int__(self):
        return self.priority

    def __lt__(self, other):
        return self._priority < other.priority

    def __str__(self):
        return "{}".format(self.name)

    def __eq__(self, other):
        return self.name == other.name and self.priority == other.priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item: QueueItem):
        heappush(self.queue, item)
        item.set_queue(self)
        return self

    def rebuild_queue(self):
        heapify(self.queue)

    def dequeue(self):
        return heappop(self.queue)

    def __len__(self):
        return len(self.queue)

    def change_el_priority(self, el, new_priority):
        index = self.queue.index(el)
        self.queue[index].priority = new_priority
