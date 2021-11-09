class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def insert(self, value): # Simplified version of insert using a helper method
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
        else:      # This will allow repeated values to be placed in the tree. To avoid this, we do: elif(value>node.value):
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def __delitem__(self, value):
        self._deleteHelper(None, self.root, value)
        return self.printInorder


    @property
    def printInorder(self):
        self._inorderHelper(self.root)      

    def _inorderHelper(self, node):
        if node is not None:
           self._inorderHelper(node.left)
           print(node.value, end=' : ')
           self._inorderHelper(node.right)
    
    


    def numChildren(self, node):
        total = 0
        if (node.left):
            total += 1
        if (node.right):
            total += 1
        return total

    def _deleteHelper(self, parent, current, value):
        if current is None:
            return None 
        if current.value>value:
            #The node in question is to the left
            self._deleteHelper(current, current.left, value) #[1]
        elif current.value<value:
            #The node in question is to the right
            self._deleteHelper(current, current.right, value) #[2]
        else:
            node_children=self.numChildren(current)
            if node_children==0 or node_children==1:
                if current.left is not None:
                    child = current.left
                else:
                    child = current.right 
                #Removing reference to current node
                if (parent is not None) and (parent.left is current):
                   parent.left = child
                elif (parent is not None) and (parent.right is current):
                    parent.right = child
                else:
                    #If root was the node that was being deleted
                    self.root = child
            else:
                temp = current.right
                parent = current
                #Find smallest value on the right subtree
                while temp.left is not None: 
                    parent = temp 
                    temp = temp.left 
                current.value= temp.value #Swap the value
                self._deleteHelper(parent, temp, temp.value) #Delete the node once swap is done
    


bst_keys = [3, 2, 5, 4, 9, 3.5, 6]
t = BinarySearchTree()
for key in bst_keys:
    t.insert(key)

t.printInorder
print()

print(t.numChildren(t.root))              # Displays 2
print(t.numChildren(t.root.left))         # Displays 0
print(t.numChildren(t.root.right))        # Displays 2
print(t.numChildren(t.root.right.right))  # Displays 1
del t[4]


