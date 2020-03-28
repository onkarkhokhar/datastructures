class BT:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    head = None


def AddNode(btree,val):
    if btree.head == None:
        btree.head = BT(val)
        return
    else:
        root = btree.head
        insert(root,val)


def insert(root,val):
    if root.left == None:
        root.left = BT(val)
        return
    elif root.right == None:
        root.right = BT(val)
        return
    else:
       return insert(root.left,val)
       return insert(root.right,val)


realBT1 = BinaryTree()
AddNode(realBT1,1)
AddNode(realBT1,2)
AddNode(realBT1,3)
AddNode(realBT1,4)
AddNode(realBT1,5)


realBT2 = BinaryTree()
AddNode(realBT2,10)
AddNode(realBT2,20)
AddNode(realBT2,30)
AddNode(realBT2,40)
AddNode(realBT2,50)
AddNode(realBT2,60)
AddNode(realBT2,70)
AddNode(realBT2,80)





def PreOrderTraversal(root):
    if root == None:
        return
    print(root.val)
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)


def InOrderTraversal(root):
    if root == None:
        return
    InOrderTraversal(root.left)
    print(root.val)
    InOrderTraversal(root.right)

def PostOrderTraversal(root):
    if root == None:
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print(root.val)

def inorderTraversal(root):
    #to maintain all left nodes
    nodes = []
    while root or nodes:
        if root:
            nodes.append(root)
            root = root.left
        else:
            present_node = nodes.pop()
            print(present_node.val)
            root = present_node.right


root1 = realBT1.head
root2 = realBT2.head
realBT3 = BinaryTree()
AddNode(realBT3,10)
root3 = realBT3.head
root3.left = BT(5)
root3.right = BT(6)
root3.right.left = BT(10)
root3.right.left.right = BT(12)
root3.right.left.left = BT(5)
root3.right.left.left.left = BT(6)

realBT4 = BinaryTree()
AddNode(realBT4,10)


#inorderTraversal(root1)
#InOrderTraversal(root1)


def heightTree(root, height):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return height
    a = heightTree(root.left, height+1)
    b = heightTree(root.right,height+1)
    return max(a,b)

def leveltraversal(root):
    if root == None:
      return
    q = []
    q.append(root)
    while q:
        cur = q.pop(0)
        print(cur.val)
        if cur.left != None:
            q.append(cur.left)
        if cur.right != None:
            q.append(cur.right)

def sizeTree(root):
    if root == None:
        return 0
    return 1+sizeTree(root.left)+sizeTree(root.right)

def countFullnode(root):
    if root == None:
        return 0
    if root.left == None or root.right == None:
        return 0
    return 1+countFullnode(root.left)+countFullnode(root.right)

def leftView(root):
    if root == None:
        return vals
    q = []
    q.append(root)
    while q:
        size = len(q)
        for i in range(size):
            cur = q.pop(0)
            if i == 0:
                print(cur.val)
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)











