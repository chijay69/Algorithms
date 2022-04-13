from time import time

# create a node blueprint aka class
class Treenode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        pass
    
    def __str__(self):    
        if self.left != None or self.right != None:
        
            return f"Node object having key: {self.key}, left: {self.left}, right: {self.right}"
        else:
        
            return f"Node object having key: {self.key}"
                 

# create node object
node0 = Treenode(3)
node1 = Treenode(4)
node2 = Treenode(5)
node3 = Treenode(6)
node4 = Treenode(7)
node5 = Treenode(8)
node6 = Treenode(9)
node7 = Treenode(10)
node8 = Treenode(11)
node9 = Treenode(12)
node10 = Treenode(13)


# assogn leaves to node0

node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
node3.left = node7
node4.left = node8
node5.right = node9
node6.left = node10



tree = node0
print(tree)

# create a list of strings in sequence
def sum_str(val):
    i=0
    mylist=[]
    while i<=val:
        mylist.append("node"+str(i))
        i+=1
    return mylist



def parse_tuple(nodetuple):
    if len(nodetuple) == 3 and isinstance(nodetuple, tuple):
        node = Treenode(nodetuple[1])
        node.left = parse_tuple(nodetuple[2])
        node.right = parse_tuple(nodetuple[0])
    elif nodetuple is None:
        node = None
    else:
        node = Treenode(nodetuple)
    return node


tree = parse_tuple(((1,3,None),2,((None,3,4),5,(6,7,8))))

print(tree)
