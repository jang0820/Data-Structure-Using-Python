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
        if len(node.childs) == 0: #在BTree最後一層
            i = self.getChild(node, x)  #找尋x要插入的小孩
            node.keys.insert(i, x)
        else:  #插入在小孩，不在BTree最後一層
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
    def  rotate(self, node, i): #相鄰節點元素足夠時，執行rotate
        if len(node.childs[i].keys) > self.order - 1:#左邊可借先借
            node.childs[i+1].keys.insert(0, node.keys[i])
            if len(node.childs[i].childs) > 0:
                node.childs[i+1].childs.insert(0, node.childs[i].childs[-1])
                node.childs[i].childs.pop(-1)
            node.keys[i] = node.childs[i].keys[-1]
            node.childs[i].keys.pop(-1)
        else:#右邊可借
            node.childs[i].keys.append(node.keys[i])
            if len(node.childs[i + 1].childs) > 0:
                node.childs[i].childs.append(node.childs[i + 1].childs[0])
                node.childs[i + 1].childs.pop(0)
            node.keys[i] = node.childs[i + 1].keys[0]
            node.childs[i + 1].keys.pop(0)
    def combine(self, node, i):
        if node == self.root and len(self.root.keys) == 1: #root只剩左右兩個小孩，合併後樹少一個階層
            tmp = self.root
            self.root = Node()
            for k in tmp.childs[0].keys:
                self.root.keys.append(k)
            self.root.keys.append(tmp.keys[0])
            for k in tmp.childs[1].keys:
                self.root.keys.append(k)
            if tmp.childs[0].childs:
                for c in tmp.childs[0].childs:
                    self.root.childs.append(c)
            if tmp.childs[1].childs:
                for c in tmp.childs[1].childs:
                    self.root.childs.append(c)
            return self.root
        else: #超過兩個以上的小孩，永遠跟右邊合併，child[i]與child[i+1]合併
            newNode = Node()
            for k in node.childs[i].keys:
                newNode.keys.append(k)
            newNode.keys.append(node.keys[i])
            for k in node.childs[i+1].keys:
                newNode.keys.append(k)
            if node.childs[i].childs :
                for c in node.childs[i].childs:
                    newNode.childs.append(c)
            if node.childs[i+1].childs :
                for c in node.childs[i+1].childs:
                    newNode.childs.append(c)
            node.keys.pop(i)
            node.childs.pop(i)
            node.childs.pop(i)  #相當於刪除node.childs[i+1]
            node.childs.insert(i, newNode)
            return node
    def search(self, node, x):  #回傳x的節點與子節點索引值
        for i in range(len(node.keys)):
            if node.keys[i] < x:
                i = i+1
            elif node.keys[i] == x:
                return (node, i) #回傳x的節點與子節點索引值
            else:
                break
        return self.search(node.childs[i], x)
    def find_right_child_min(self, node):    #輸入node為右子樹，取右子樹的最小
        while len(node.childs) > 0:
            node = node.childs[0]
        return node.keys[0]
    def delete(self, node, x):
        node, i = self.search(node, x)
        if len(node.childs) == 0:   #x在B-Tree的最後一層
            self.delete_last_level(self.root, x)
        else:
            y = self.find_right_child_min(node.childs[i+1]) #node.childs[i+1]為右子樹，找到右子樹的最小值儲存到變數y
            self.delete_last_level(self.root, y)   #y在B-Tree的最後一層，直接刪除y
            node, i = self.search(self.root, x)
            node.keys[i] = y   #將x取代為y
    def delete_last_level(self, node, x):
        finish = False
        for i in range(len(node.keys)):
            if node.keys[i] < x:
                i = i + 1
            elif node.keys[i] == x:
                node.keys.pop(i)  #刪除x
                finish = True
                return finish
            else:
                break
        if finish == False and len(node.childs[i].keys) == self.order - 1: #節點個數只符合B-Tree的最少個數
            if i == 0: #最左邊
                if len(node.childs[i+1].keys) > self.order - 1:  #右子樹的節點數多於B-Tree的最少個數，使用旋轉
                    self.rotate(node, i)
                else:
                    node = self.combine(node, i)   #右子樹的節點數也是B-Tree的最少個數，使用合併
                    return self.delete_last_level(node, x)
            elif i == len(node.childs) - 1 : #最右邊
                if len(node.childs[i-1].keys) > self.order - 1:  #左子樹的節點數多於B-Tree的最少個數，使用旋轉
                    self.rotate(node, i-1)
                else:
                    node = self.combine(node, i-1) #合併只有向右合併，所以i-1
                    return self.delete_last_level(node, x)
            else:  #在中間的子樹
                if  len(node.childs[i+1].keys) > self.order - 1: #右邊相鄰的子樹節點數夠多，使用旋轉
                    self.rotate(node, i)
                elif len(node.childs[i-1].keys) > self.order - 1:  #左邊相鄰的子樹節點數夠多，使用旋轉
                    self.rotate(node, i-1)
                else:
                    node = self.combine(node, i)
                    return self.delete_last_level(node, x)
        i = self.getChild(node, x)
        return self.delete_last_level(node.childs[i], x)
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
data = [36, 83, 85, 93, 12, 98, 2, 6, 57, 79]
for item in data:
    btree.insert(item)
    btree.print_btree()
data = [2, 93, 6, 12, 83, 36, 85, 79, 57, 98]
for item in data:
    btree.delete(btree.root, item)
    btree.print_btree()