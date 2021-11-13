#Lab #7
#Due Date: 11/12/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.

class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        if len(self._heap) == 0:
            return None
        return self._heap[0]
    
    #Passes in a Heap Index (1-indexed)
    #Returns value of the parent
    def _parent(self,index):
        if index == 1:
            return None
        return self._heap[index//2 -1]

    #Passes in a Heap Index (1-Indexed)
    #Returns value of left child
    def _leftChild(self,index):
        n = 2*index - 1
        if n >= len(self._heap):
            return
        return self._heap[n]
    #Passes in a Heap Index (1-Indexed)
    #Returns the value of right child
    def _rightChild(self,index):
        n = 2*index
        if n >= len(self._heap):
            return
        return self._heap[n]
    
    #Inserts a new item into the heap and may update current minimum
    def insert(self,item):
        '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        '''
        self._heap.append(item)
        #Heap Index of Item
        k = len(self._heap)
        #While there is a parent and the child dominates the parent
        while (self._parent(k) != None) and self._parent(k) > self._heap[k-1]:
            #Swap the child and the parent
            self._heap[k-1], self._heap[k//2 -1] = self._heap[k//2 - 1], self._heap[k-1]
            #Update the current position of the node in question
            k = k//2


    #Deletes the current minimum from the heap and updates the heap with a new minimum
    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted=self._heap[0]
            self._heap=[]
            return deleted
        else:
            #Swap the current min with the rightmost leaf
            self._heap[0], self._heap[len(self._heap)-1] = self._heap[len(self._heap)-1], self._heap[0]
            #Delete rightmost leaf
            oldMin = self._heap.pop(len(self._heap)-1)
            k=1 #Position Tracker

            #Bubble the current min down until it finds the current place
            #While they are two children, and one of them dominates their parent, swap the parent down
            while (self._leftChild(k) != None) and (self._rightChild(k) != None) and ((self._leftChild(k) < self._heap[k-1]) or (self._rightChild(k) < self._heap[k-1])):  
                #If the left child dominates rightchild, swap left child and parent
                if self._leftChild(k) < self._rightChild(k):
                    self._heap[k-1], self._heap[2*k -1] = self._heap[2*k - 1], self._heap[k-1]
                    k = 2*k
                #If right child dominates leftchild, swap right child and parent
                else: 
                    self._heap[k-1], self._heap[2*k] = self._heap[2*k], self._heap[k-1]
                    k = 2*k+1
            #Added one edge case when the element has only one child
            if self._leftChild(k) and self._leftChild(k) < self._heap[k-1]:
                self._heap[k-1], self._heap[2*k -1] = self._heap[2*k - 1], self._heap[k-1]
                k = 2*k
            return oldMin

#Returns a sorted list, sorts it by constructing a heap and repeatedly selecting the minimum
def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    #Constructs a heap with the elements of the list
    heap = MinBinaryHeap()
    for item in numList: 
        heap.insert(item)
    newList=[]
    #While the heap is not empty, append the next minimum to the heap
    while heap.getMin != None:
        newList.append(heap.deleteMin())
    return newList

'''
if __name__ == '__main__':
    import doctest
    doctest.run_docstring_examples(heapSort, globals(), name='LAB7', verbose=True)
'''
