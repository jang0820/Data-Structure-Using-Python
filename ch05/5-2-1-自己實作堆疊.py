class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [0]*self.size
        self.top = -1
    def isFull(self):
        return self.top == self.size-1
    def isEmpty(self):
        return self.top == -1
    def push(self, x):
        if self.isFull():
            print("堆疊已滿")
        else:
            self.top = self.top + 1
            self.data[self.top] = x
    def pop(self):
        if self.isEmpty():
            print("堆疊是空的")
        else:
            item = self.data[self.top]
            self.top = self.top - 1
            return item
    def printStack(self):
        for i in range(0, self.top + 1):
            print(self.data[i], end="")
        print()
st = Stack(4)
for i in range(1, 5):
    st.push(i)
    st.printStack()
for i in range(1, 5):
    st.pop()
    st.printStack()

