class Queue:
    def __init__(self, size):
        self.size = size
        self.data = [0]*self.size
        self.front = -1
        self.back = -1
    def isFull(self):
        return self.back == self.size-1
    def isEmpty(self):
        return self.back == self.front
    def enQueue(self, x):
        if self.isFull():
            print("佇列已滿")
        else:
            self.back = self.back + 1
            self.data[self.back] = x
    def deQueue(self):
        if self.isEmpty():
            print("佇列是空的")
        else:
            self.front = self.front + 1
            return self.data[self.front]
    def printQueue(self):
        for i in range(self.front + 1, self.back + 1):
            print(self.data[i], end="")
        print()
q = Queue(4)
for i in range(1, 5):
    q.enQueue(i)
    q.printQueue()
for i in range(1, 5):
    q.deQueue()
    q.printQueue()

