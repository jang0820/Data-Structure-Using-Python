class CirQueue:
    def __init__(self, size):
        self.size = size
        self.data = [0]*self.size
        self.front = 0
        self.back = 0
    def isFull(self):
        return self.front == ((self.back + 1) % self.size)  # 浪費一個空間
    def isEmpty(self):
        return self.back == self.front
    def enQueue(self, x):
        if self.isFull():
            print("環狀佇列已滿")
        else:
            self.data[self.back] = x
            self.back = (self.back + 1) % self.size
    def deQueue(self):
        if self.isEmpty():
            print("環狀佇列是空的")
        else:
            item = self.data[self.front]
            self.front = (self.front + 1) % self.size
            return item
    def printQueue(self):
        if not self.isEmpty():
            if self.back > self.front:
                for i in range(self.front, self.back):
                    print(self.data[i] ,end="")
            else:
                for i in range(self.front, self.size):
                    print(self.data[i], end="")
                for i in range(0, self.back):
                    print(self.data[i], end="")
        print()
q = CirQueue(5)
for i in range(1, 5):
    q.enQueue(i)
    q.printQueue()
for i in range(1, 5):
    q.deQueue()
    q.printQueue()

