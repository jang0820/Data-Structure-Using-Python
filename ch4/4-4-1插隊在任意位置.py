class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertHead(self, x):
        self.head = Node(x)
    def insertAt(self, x, pos): # x插入在pos位置
        tmp = self.head
        nodex = Node(x)
        count = 2
        if pos == 1: #插入在第一個位置
            nodex.next = tmp
            self.head = nodex
        else:
            while count < pos:
                tmp = tmp.next
                count = count + 1
            nodex.next = tmp.next
            tmp.next = nodex
    def remove(self, x):
        tmp =self.head
        while tmp != None:
            if tmp.data == x:
                break
            before = tmp
            tmp = tmp.next
        if tmp == self.head:  #刪除第一個元素
            self.head = self.head.next
        else:
            before.next = tmp.next
    def serve(self):
        item = self.head
        self.head = self.head.next
        return item.data
n, m = input().split()
n = int(n)
m = int(m)
li = LinkedList()
li.insertHead(1)
for i in range(2, n+1):
    li.insertAt(i, i)
for i in range(m):
    cmd = input()
    if cmd[0] == "s":
        x = li.serve()
        li.insertAt(x, n)
        print(x)
    else:
        p, x, pos = cmd.split()
        x = int(x)
        li.remove(x)
        pos = int(pos)
        li.insertAt(x, pos)
