class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return 'Head:{}\nTail:{}\nList: {}'.format(self.head,self.tail,out)

    __repr__=__str__

    def replace(self, new,  a, b=-2):
        '''
        >>> lst1 = LinkedList()
        >>> lst1.add(5) 
        >>> lst1.add(6) 
        >>> lst1.add(9) 
        >>> lst1.add(10) 
        >>> lst1.add(0)
        >>> lst1.add(8)
        >>> lst2 = LinkedList()
        >>> lst2.add('a')
        >>> lst2.add('b')
        >>> lst2.add('c')
        >>> lst1
        Head:Node(8)
        Tail:Node(5)
        List: 8 -> 0 -> 10 -> 9 -> 6 -> 5
        >>> lst2
        Head:Node(c)
        Tail:Node(a)
        List: c -> b -> a
        >>> lst1.replace(lst2, 2, 4)
        >>> lst1 
        Head:Node(8)
        Tail:Node(5)
        List: 8 -> 0 -> c -> b -> a -> 6 -> 5
        '''
        #Keeps track of where to add new nodes
        connectStart = connectEnd = None
        temp = self.head
        i = 0 #Index to keep track of where one is
        while temp:
            #If the node is right before the connection point
            if (i == (a-1)):
                connectStart = temp
            if (i == b):
                connectEnd = temp
            i += 1
            temp = temp.next

        #Splicing the two lists together
        connectStart.next = new.head
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = connectEnd
        
        #Updating the tail
        while temp.next:
            temp = temp.next
        self.tail = temp

    def isEmpty(self):
        return self.head==None


    def __len__(self):
        current=self.head
        count=0
        while current is not None:
            count += 1
            current = current.next    
        return count


    def add(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode


    def __contains__(self,value):
        current=self.head
        while current is not None:
            if current.value==value:
                return True
            else:
                current=current.next
        return False


    def __delitem__(self,position):   
        if self.isEmpty():
            print('List is empty')
            return None
        if len(self)>=position:
            current=self.head
            previous=None
            count=1
            while count<position:
                    previous=current
                    current=current.next
                    count+=1
            if previous is None:
                self.head=current.next
                current.next=None
            elif current.next is None:
                previous.next=None
                self.tail=previous
            else:
                previous.next=current.next
                current.next=None

    def append(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def __getitem__(self,value):
        current=self.head
        while current is not None:
            if current.value==value:
                return current
            else:
                current=current.next
        return None

    def pop(self):
        if self.isEmpty():
            print('List is empty')
            return None
        else:
            removed = self.tail.value
            if len(self) == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next.next is not None:
                    current = current.next

                current.next = None
                self.tail = current
            return removed            
