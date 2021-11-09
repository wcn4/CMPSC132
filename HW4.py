# HW4
# Due Date: 11/05/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.
#       You might add additional methods to encapsulate and simplify the operations, but they must be
#       thoroughly documented


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
        >>> x.insert('mom')  
        >>> x.insert('omm') 
        >>> x.insert('mmo') 
        >>> x.root          
        Node({'mmo': ['mom', 'omm', 'mmo']})
        >>> x.insert('sat')
        >>> x.insert('kind')
        >>> x.insert('ats') 
        >>> x.root.left
        Node({'ast': ['sat', 'ats']})
        >>> x.root.right is None
        True
        >>> x.root.left.right
        Node({'dikn': ['kind']})
    '''

    #Initializes root to be zero, and the number of words and nodes stored to zero
    def __init__(self):
        self.root = None
        self._words = 0
        self._nodes = 0


    # Modify the insert and _insert methods to allow the operations given in the PDF
    def insert(self, value):
        #The value is set to a tuple with the sorted key to a list, the original value
        #''.join(sorted(x)) returns the alphabetically sorted key
        #Reason why it is a tuple is because fixed size, and easier to pass the sorted value and 
        #original value rather than recomputing the sorted value every single time
        self._words += 1
        value = (''.join(sorted(value)), value)
        if self.root is None:
            self.root=Node({value[0]:[value[1]]})
            self._nodes += 1
        else:
            self._insert(self.root, value)


    #Helper function to insert values (takes a tuple in the form (sorted, original))
    def _insert(self, node, value):
        #If the keys are equal
        if value[0] in node.value:
            #Append the original word into the node's dictionary
            node.value[value[0]].append(value[1])
            return
        #Use comparison function to determine whether to go left or right (since they aren't equal)
             # list(node.value)[0] is a not so elegant way of getting the only key in the node given
             # that the value is unknown. 
        if(self._compareKey(value[0], list(node.value)[0])):
            if(node.left==None):
                #Create a node with the dictionary (sorted:[original])
                node.left = Node({value[0]:[value[1]]})
                self._nodes += 1
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                #Create a node with the dictionary (sorted:[original])
                node.right = Node({value[0]:[value[1]]})
                self._nodes += 1
            else:
                self._insert(node.right, value)
    
    #Takes two non-equal strings and returns a boolean on whether a < b
    #Compares them alphabetically (using ordinal values), from first index to last index
    def _compareKey(self, a, b):
        #Compares every character up until the max length of either string (to avoid indexing errors)
        for i in range(0, min(len(a), len(b))):
            if ord(a[i]) < ord(b[i]):
                return True
            if ord(a[i]) > ord(b[i]):
                return False
        #If one is a substring of another, return whether a is substring of b
        return (len(a) < len(b))

    def isEmpty(self):
        return self.root == None

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

    



class Anagrams:
    '''
        # Verify class has _bst attribute  
        >>> x = Anagrams(5)
        >>> '_bst' in x.__dict__    
        True
        >>> isinstance(x.__dict__.get('_bst'), BinarySearchTree)
        True
        >>> x = Anagrams(5)
        >>> x.create('words_small.txt')
        >>> x.getAnagrams('tap')
        'No match'
        >>> x.getAnagrams('arm')
        'No match'
        >>> x.getAnagrams('rat')
        ['art', 'tar', 'rat']
        >>> x._bst.printInorder
        {'a': ['a']} : {'adns': ['ands', 'sand']} : {'ahms': ['sham', 'hams']} : {'amt': ['tam', 'mat']} : {'arst': ['arts', 'rats', 'star']} : {'arsty': ['artsy']} : {'art': ['art', 'tar', 'rat']} : 
        
        #Medium txt Tests
        >>> x = Anagrams(5)
        >>> x.create('words_medium.txt')
        >>> x.getAnagrams('sale')
        ['ales', 'leas', 'sale', 'seal']
        >>> x.getAnagrams('love')
        'No match'
        >>> x.getAnagrams('mean')
        ['amen', 'mane', 'mean', 'name']
        >>> x._bst._words
        487
        >>> x._bst._nodes
        134

        >>> x = Anagrams(6)
        >>> x.create('words_medium.txt')
        >>> x._bst._words
        720
        >>> x._bst._nodes
        201
        >>> x = Anagrams(3)
        >>> x.create('words_large.txt')
        >>> x._bst._words
        1067
        >>> x._bst._nodes
        784
        
        >>> x = Anagrams(5)
        >>> x.create('words_large.txt')
        >>> x._bst._words
        13602
        >>> x._bst._nodes
        9747
        >>> x = Anagrams(9)
        >>> x.create('words_large.txt')
        >>> x._bst._words
        105175
        >>> x._bst._nodes
        89890
    '''
    
    def __init__(self, word_size):
        self.maxSize = word_size
        self._bst = BinarySearchTree()



    def create(self, file_name):
        # -YOUR CODE STARTS HERE
        # Code for reading the contents of file_name is given in the PDF
        with open(file_name) as f:
            contents = f.read()
            #Split by the line
            for word in contents.splitlines(): 
                #If the word is at least one character long and is less than or equal to maxsize
                if len(word) <= self.maxSize and len(word) != 0:
                    self._bst.insert(word)

    #Returns the list of all anagrams in the tree
    def getAnagrams(self, word):
        return self._getAnagrams(self._bst.root, ''.join(sorted(word)))

    #The helper function for getAnagrams. 
    #Searches through the tree using the bst_compareKey function
    def _getAnagrams(self, node, key):
        if not node: 
            return 'No match'
        #If key = dict.key, return list
        if key in node.value:
            return node.value[key]
        #If key < dict.key, go left, otherwise go right
        if self._bst._compareKey(key, list(node.value)[0]):
            return self._getAnagrams(node.left, key)
        return self._getAnagrams(node.right, key)

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(Anagrams, globals(), name='HW4', verbose=True)
