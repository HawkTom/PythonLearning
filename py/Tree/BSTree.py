class BSTreeNode(object):

    def __init__(self, data):
        self.val = data
        self.leftChild = None
        self.rightChild = None


# 建立二叉树是以层序遍历方式输入，节点不存在时以 'None' 表示
def creatTree(nodeList):
    if nodeList[0] == None:
        return None
    head = BSTreeNode(nodeList[0])
    Nodes = [head]
    j = 1
    for node in Nodes:
        if node != None:
            node.leftChild = (BSTreeNode(nodeList[j]) if nodeList[j] != None else None)
            Nodes.append(node.leftChild)
            j += 1
            if j == len(nodeList):
                return head
            node.rightChild = (BSTreeNode(nodeList[j])if nodeList[j] != None else None)
            j += 1
            Nodes.append(node.rightChild)
            if j == len(nodeList):
                return head

# head为二叉树的根节点
# 前序遍历方式遍历二叉树
def PreorderTraverse(head):
    if head:
        print(head.val)
        PreorderTraverse(head.leftChild)
        PreorderTraverse(head.rightChild)

# 中序遍历方式 遍历二叉树
def InorderTrverse(head):
    if head:
        InorderTrverse(head.leftChild)
        print(head.val)
        InorderTrverse(head.rightChild)

# 后续遍历方式遍历二叉树
def PostorderTraverse(head):
    if head:
        PostorderTraverse(head.leftChild)
        PostorderTraverse(head.rightChild)
        print(head.val)

# a = [0,2,None,3,4,5]
# a = [0,1,2,3,4,5,6]
a = [1,2,3,4,5,None,6,None,None,7,8]
# a = list("ABCD")+[None] + list("RTYI")
t = creatTree(a)
InorderTrverse(t)
print("OK")
