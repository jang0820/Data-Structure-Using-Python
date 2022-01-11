class BinaryTree:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right  
p1 = BinaryTree('A')
root = p1
p2 = BinaryTree('B')
p3 = BinaryTree('C')
p4 = BinaryTree('D')
p5 = BinaryTree('E')
p7 = BinaryTree('F')
p1.setLeft(p2)
p1.setRight(p3)
p2.setLeft(p4)
p2.setRight(p5)
p3.setRight(p7)
