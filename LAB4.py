# LAB4
# Due Date: 10/08/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.replicate()
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> -7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 8.76 -> 9.78 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

    
    #Preforms an insertion sort on the singly linked list
    def add(self, value):
        newNode = Node(value)
        #If there is no head, insert it 
        if not self.head: 
            self.head = newNode
            self.tail = newNode
            return

        #If it goes at the front of the list, append it to the front
        if value <= self.head.value:
            newNode.next = self.head
            self.head = newNode
            return
        
        #Iterate through the list seeing if newNode can be inserted before a certain element
        temp = self.head
        while temp.next: #As long as there is a next node
            #If the node can be inserted at the spot after the current node, insert it
            if (temp.value <= value and value <= temp.next.value):
                newNode.next = temp.next
                temp.next = newNode
                return
            temp = temp.next
        #If it it could not be inserted then, append it to the end.
        self.tail.next = newNode
        self.tail = newNode


    #Will return a new list based off the current list where each node is repeated node.value times in the new list. (Will do it 2x for floats and negatives, once for 0)
    def replicate(self):
        newList = SortedLinkedList()
        temp = self.head
        #For each node in the list
        while temp:
            #If it is zero, add it once
            if (temp.value == 0):
                newList.add(temp.value)
            #If it is a float or negative, add it twice
            if (temp.value < 0 or isinstance(temp.value, float)):
                newList.add(temp.value)
                newList.add(temp.value)
            else:
            #Otherwise, add it node.value times
                for x in range(temp.value):
                    newList.add(temp.value)
            temp = temp.next
        return newList

    #Removes all duplicates in the list
    def removeDuplicates(self):
        #Since the list is sorted, all duplicates will be next to each other
        temp = self.head
        while temp:
            #If a next node exists and that value is equal to the current node's value
            while (temp.next and temp.next.value == temp.value):
                #Delete it
                temp.next = temp.next.next
            temp = temp.next 
