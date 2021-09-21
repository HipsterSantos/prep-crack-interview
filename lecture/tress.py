class BinaryTree:
    def __init__(self):
        self._root = null
    def traversePreOrderHelper(self,node:Node):
        """root-> left-> right"""
        traversePreOrderHelper(self._root)
        if not node :
            return
        print(node.data)
        traversePreOrderHelper(node.left)
        traversePreOrserHelper(node.right)
    #implementing this version interactively 
    def traversePreOrderIntertive(self):
        var nodeStack = []
        nodeStack.append(self._root)
        """
        Logic for this solution 
        pop all itmes obe by one. Do following for every popper item 
        -print it 
        push its right child 
        push its lfef child 

        """
        pass 
    def traverseInOrderHelper(self,node):
        traverseInOrderHelper(self._root)
        """
        left->root->right
        """
        if not node:
            return 
        traverseInOrderHelper(node.left)
        print(node.data)
        traveseInOrderHelper(node.right)

class Node:
    def __init__(self,data):
        self.data = data 
        self.left  = null 
        self.right = null 
    def find_sum(root):

class Tree():
    def __init__(self):
        self.root = null