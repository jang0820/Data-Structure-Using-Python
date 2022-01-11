class AVLTree:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1
    def getHeight(self, node):
        if node == None:
            return 0
        else:
            return node.height
    def updateHeight(self, node):
        if self.getHeight(node.left) > self.getHeight(node.right):
            node.height = self.getHeight(node.left) + 1
        else:
            node.height = self.getHeight(node.right) + 1
    def LL(self, node):
        left = node.left
        left_right = left.right
        left.right = node
        left.right.left = left_right
        self.updateHeight(left.right)  #left.right的高度有變更，需要更新
        self.updateHeight(left)        #left的高度有變更，需要更新
        return left
    def RR(self, node):
        right = node.right
        right_left = right.left
        right.left = node
        right.left.right = right_left
        self.updateHeight(right.left)
        self.updateHeight(right)
        return right
    def LR(self, node):
        left = node.left
        left_right = left.right
        left_right_left = left_right.left
        left_right_right = left_right.right
        left_right.left = left
        left_right.right = node
        left_right.left.right = left_right_left
        left_right.right.left = left_right_right
        self.updateHeight(left_right.left)
        self.updateHeight(left_right.right)
        self.updateHeight(left_right)
        return left_right
    def RL(self, node):
        right = node.right
        right_left = right.left
        right_left_left = right_left.left
        right_left_right = right_left.right
        right_left.left = node
        right_left.right = right
        node.right = right_left_left 
        right.left = right_left_right
        self.updateHeight(right_left.left)
        self.updateHeight(right_left.right)
        self.updateHeight(right_left)
        return right_left
    def leftBalance(self, node, x):
        if x < node.left.val: #LL
            node = self.LL(node)
        else: #LR
            node = self.LR(node)
        return node
    def rightBalance(self, node, x):
        if x < node.right.val: #RL
            node = self.RL(node)
        else: #RR
            node = self.RR(node)
        return node
    def insertNode(self, node, x):
        if node != None:
            if node.val > x:
                node.left = self.insertNode(node.left, x)
                if abs(self.getHeight(node.left) - self.getHeight(node.right)) == 2:
                    node = self.leftBalance(node, x)
            else:
                node.right = self.insertNode(node.right, x)
                if abs(self.getHeight(node.left) - self.getHeight(node.right)) == 2:
                    node = self.rightBalance(node, x)
        else:
            node = AVLTree(x)
        self.updateHeight(node)
        return node
    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.val, " ", sep="", end="")
            self.inorder(node.right)
    def search(self, node, x):
        if node == None:
            return False
        if node.val == x:
            return True
        elif node.val > x:
            return self.search(node.left, x)
        else:
            return self.search(node.right, x)
root = AVLTree(7)
data = [3, 10, 8, 13, 9]
for i in range(len(data)):
    root = root.insertNode(root, data[i])
    root.inorder(root)
    print()
print(root.search(root, 13))




