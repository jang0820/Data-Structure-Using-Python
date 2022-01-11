class Node:
    def __init__(self):
        self.childs = []
        self.keys = []
class BTree:
    def __init__(self, order):
        self.order = order
        self.root = Node()
    def getChild(self, node, x):  # x在node的第幾個小孩下
        for i in range(len(node.keys)):
            if node.keys[i] < x:
                i = i+1
            else:
                return i
        return len(node.keys)
    def insert(self, x): #
        if len(self.root.keys) == 2*self.order -1: #root滿了，增加一層
            tmp = self.root
            self.root = Node()
            self.root.childs.append(tmp)
            self.split(self.root, 0)  #root.childs[0]一分為二，也就是將tmp一分為二
            if self.root.keys[0] < x:
                self.insert2(self.root.childs[1], x)
            else:
                self.insert2(self.root.childs[0], x)
        else:
            self.insert2(self.root, x)
    def insert2(self, node, x): #從root下來，滿了先split
        if len(node.childs) == 0: #在BTree最下層
            i = self.getChild(node, x)  #找尋x要插入的小孩
            node.keys.insert(i, x)
        else:  #插入在小孩，不在BTree最下層
            i = self.getChild(node, x)  #找尋x要插入的小孩
            if len(node.childs[i].keys) == 2*self.order -1: #小孩滿了，雙親節點node未滿
                self.split(node, i)  #node.childs[i]一分為二
                if node.keys[i] < x:
                    i = i+1
                self.insert2(node.childs[i], x)
            else:     #小孩未滿
                self.insert2(node.childs[i], x)
    def split(self, node, i):
        #將node.child[i]一分為二，取中間元素插入雙親節點node內，node.child[i]的所有keys與childs分割成兩個node，加入雙親節點node的小孩
        tmp = node.childs[i]
        node.keys.insert(i, tmp.keys[self.order - 1])   #取node.childs[i].keys的中間節點插入到雙親節點node的keys
        right = Node()
        left = Node()
        right.keys = tmp.keys[self.order: 2 * self.order - 1]     #keys分割成兩個
        left.keys = tmp.keys[0: self.order - 1]                   #keys分割成兩個
        if len(tmp.childs) > 0:  #若tmp.childs不是空串列
            right.childs = tmp.childs[self.order : 2*self.order]  #childs分割成兩個
            left.childs = tmp.childs[0 : self.order]              #childs分割成兩個
        node.childs[i] = left
        node.childs.insert(i+1, right)
    def print_btree(self):
        node = [(self.root, 1)]
        while len(node) > 0:
            n,i = node.pop(0)
            if len(node)>0 and i == node[0][1]:
                print(n.keys, end="")
            else:
                print(n.keys)
            if n.childs != []:
                i = i + 1
                for c in n.childs:
                    node.append((c,i))
        print()
btree = BTree(3)  #分支度最大為6，分支度最小為3的Btree，也就是節點的最多元素個數為5，最少元素個數為2
data = [36, 2, 6, 57, 12, 98, 79, 83, 85, 93]
for item in data:
    btree.insert(item)
    btree.print_btree()


