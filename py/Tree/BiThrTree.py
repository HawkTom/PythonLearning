from enum import Enum

class tag(Enum):
    Link = 0
    Thread = 1

class BiThrTree(object):

    def __init__(self, data):
        self.val = data
        self.ltag = tag.Link
        self.rtag = tag.Link
        self.leftChild = None
        self.rightChild = None


def creatTree(nodeList):
    if nodeList[0] == None:
        return None
    head = BiThrTree(nodeList[0])
    Nodes, j = [head], 1
    for node in Nodes:
        if node != None:
            node.leftChild = (BiThrTree(nodeList[j]) if nodeList[j] != None else None)
            Nodes.append(node.leftChild)
            j += 1
            if j == len(nodeList):
                return head
            node.rightChild = (BiThrTree(nodeList[j]) if nodeList[j] != None else None)
            Nodes.append(node.rightChild)
            j += 1
            if j == len(nodeList):
                return head

pre = BiThrTree('#')
def InorderTraverse(root):
    global pre
    if root:
        InorderTraverse(root.leftChild)
        if not root.leftChild:
            root.ltag = tag.Thread
            root.leftChild = pre
        if not pre.rightChild:
            pre.rtag = tag.Thread
            pre.rightChild = root
        pre = root
        InorderTraverse(root.rightChild)




a = list("ABCD")+[None,None]+list('EFG')
t = creatTree(a)
InorderTraverse(t)
print("OK")




