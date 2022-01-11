class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self, x):
        self.root = Node(x)
    def insert(self, now, x):
        if now == None:
            now = Node(x)
        elif now.val > x:
            if now.left == None:
                now.left = Node(x)
            else:
                self.insert(now.left, x)
        else:
            if now.right == None:
                now.right = Node(x)
            else:
                self.insert(now.right, x)
    def search(self, now, x):
        if now == None:
            return False
        if now.val == x:
            return True
        elif now.val > x:
            return self.search(now.left, x)
        else:
            return self.search(now.right, x)
    def delete(self, now, x):  #假設x存在於二元搜尋樹內
        if now.val > x:
            now.left = self.delete(now.left, x)
        elif now.val < x:
            now.right = self.delete(now.right, x)
        else:
            if now.left != None and now.right != None:
                tmp = now.right
                while tmp.left != None:
                    tmp = tmp.left
                now.val = tmp.val
                now.right = self.delete(now.right, now.val)
            else:
                if now.left == None:
                    now = now.right
                else:
                    now = now.left
        return now
    def search_and_delete(self, now, x):
        if self.search(self.root, x):
            self.root = self.delete(self.root, x)
def inorder(p):
    if p != None:
        inorder(p.left);
        print(p.val, ' ', end='');
        inorder(p.right);
bst = BinarySearchTree(10)
bst.insert(bst.root, 5)
bst.insert(bst.root, 3)
bst.insert(bst.root, 7)
bst.insert(bst.root, 12)
bst.insert(bst.root, 11)
bst.insert(bst.root, 13)
inorder(bst.root)
print()
bst.search_and_delete(bst.root, 5)
inorder(bst.root)
print()
bst.search_and_delete(bst.root, 10)
inorder(bst.root)
print()
bst.search_and_delete(bst.root, 11)
inorder(bst.root)
print()
bst.search_and_delete(bst.root, 13)
inorder(bst.root)
print()
bst.search_and_delete(bst.root, 12)
inorder(bst.root)
print()
bst.search_and_delete(bst.root, 7)
inorder(bst.root)
print()
bst.search_and_delete(bst.root, 3)
inorder(bst.root)
