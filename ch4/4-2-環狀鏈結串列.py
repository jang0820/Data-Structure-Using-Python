class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
class CirLinkedList:
    def __init__(self):
        self.head = None
    def insertHead(self, x):
        self.head = Node(x)
        self.head.next = self.head
    def insert(self, y, x): # 在y後面插入x
        tmp = self.head
        nodex = Node(x)
        while True:
            if tmp.data == y:
                break
            tmp = tmp.next
        nodex.next = tmp.next
        tmp.next = nodex
    def remove(self, x):
        before = self.head
        tmp =self.head.next
        while True:
            if tmp.data == x:
                break
            before = tmp
            tmp = tmp.next
        if tmp == self.head and self.head.next == self.head:  #只剩一個元素
            self.head = None
        elif tmp == self.head:  #刪除第一個元素
            self.head = self.head.next
            before.next = self.head
        else:
            before.next = tmp.next
    def len(self):
        count = 0
        if self.head == None:
            return 0
        else:
            tmp = self.head.next
            while tmp != self.head:
                count = count + 1
                tmp = tmp.next
            return count + 1
    def printLinkedList(self):
        length = self.len()
        tmp = self.head
        for i in range(length):
            print(tmp.data, " ", end="")
            tmp = tmp.next
        print()
li = CirLinkedList()
li.insertHead(5)
for i in range(6, 10):
    li.insert(i-1,i)
    li.printLinkedList()
for i in range(5, 10):
    li.remove(i)
    li.printLinkedList()

