btree=[None]*1024
btree[1]='A'
btree[2]='B'
btree[3]='C'
btree[4]='D'
btree[5]='E'
btree[7]='F'
def preorder(p):
    if btree[p]:
        print(btree[p], ' ', end='');
        preorder(2*p);
        preorder(2*p+1);
def inorder(p):
    if btree[p]:
        inorder(2*p);
        print(btree[p], ' ', end='');
        inorder(2*p+1);
def postorder(p):
    if btree[p]:
        postorder(2*p);
        postorder(2*p+1);
        print(btree[p], ' ', end='');
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
