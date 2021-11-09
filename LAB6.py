# Lab #6


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
        >>> new_tree = x.mirror()
        11 : 10 : 9.5 : 9 : 7 : 5 : 4 : 2 : 
        >>> new_tree.root.right
        Node(4)
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)         


    @property
    def printPreorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._preorderHelper(self.root)
        
    def _preorderHelper(self, node):
        if node is not None:
            print(node.value, end=' : ') 
            self._preorderHelper(node.left) 
            self._preorderHelper(node.right)         
    
    @property
    def printPostorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._postorderHelper(self.root)
        
    def _postorderHelper(self, node):
        if node is not None:
            self._postorderHelper(node.left) 
            self._postorderHelper(node.right)
            print(node.value, end=' : ')

    def mirror(self):
        # Creates a new BST that is a mirror of self: Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree
        



    #A tree is empty if there is no root, as all nodes are indirectly connected to the root
    def isEmpty(self):
        return not (self.root)


    #Creates a mirrored copy of the tree
    def _mirrorHelper(self, node):
        #If the node is empty return nothing
        if not node:
            return
        #Copy the current value
        newNode = Node(node.value)
        #Copy the original node's right tree to the new Node's left
        newNode.left = self._mirrorHelper(node.right)
        #Copy the original node's left tree to the new Node's right
        newNode.right = self._mirrorHelper(node.left)
        return newNode

    #Returns the minimum value within the tree
    @property
    def getMin(self): 
        #Traveler node
        temp = self.root
        #While there is a left node
        while (temp.left):
            temp = temp.left
        #Since tree is sorted, this is the min.
        return temp

    #Returns the maximum value within the tree
    @property
    def getMax(self): 
        #Traveler node
        temp = self.root
        #While there is a left node
        while (temp.right):
            temp = temp.right
        #Since tree is sorted, this is the min.
        return temp


    #Determines whether a node with a certain value is within a tree
    def __contains__(self,value):
        return self.__containshelper(self.root, value)

    #The recursive helper function for __contains__
    def __containshelper(self,node,value):
        #If there is no node, it does not contain the value
        if not node:
            return False
        #If the node with the desired value has been found, return true
        if (node.value == value):
            return True
        #Return true if the node has been found in the left or right subtrees
        return self.__containshelper(node.left, value) or self.__containshelper(node.right, value)

    #Returns the height of the tree
    def getHeight(self, node):
        #If the node is null, return a height of -1
        #This is done such that when the parent adds +1 to each connection to children, an edge to a null child has a depth of 0
        if not node:
            return -1
        #If the node is a leaf, it has a height of zero
        if not node.left and not node.right:
            return 0
        #Get the height of both subtrees
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        #Add one to the greater subtree to account for the edge connecting the parent to the child
        if leftHeight >= rightHeight:
            return leftHeight+1
        return rightHeight+1


x = BinarySearchTree()
nums = [47,5,3,70,23,53,15,66,81,64,85,31,83,33,9,7]
for i in nums:
    x.insert(i)
print("Preorder: ")
x.printPreorder
print()
print("In order: " )
x.printInorder
print()
print("Post order: ")
x.printPostorder
