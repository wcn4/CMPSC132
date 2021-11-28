# HW5
# Due Date: 11/19/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.


class Node:
    def __init__(self, content):
        self.value = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class ContentItem:
    '''
        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content3 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content4 = ContentItem(1005, 18, "another header", "111110")
        >>> hash(content1)
        0
        >>> hash(content2)
        1
        >>> hash(content3)
        2
        >>> hash(content4)
        1
    '''
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return f'CONTENT ID: {self.cid} SIZE: {self.size} HEADER: {self.header} CONTENT: {self.content}'

    __repr__=__str__

    def __eq__(self, other):
        if isinstance(other, ContentItem):
            return self.cid == other.cid and self.size == other.size and self.header == other.header and self.content == other.content
        return False

    #Computes the Hash value based off the sum of all ASCII characters
    #in the header mod 3
    def __hash__(self):
        total = 0
        for char in self.header:
            total += ord(char)
        return total%3


class CacheList:
    ''' 
        # An extended version available on Canvas. Make sure you pass this doctest first before running the extended version

        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content3 = ContentItem(1005, 180, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content4 = ContentItem(1006, 18, "another header", "111110")
        >>> content5 = ContentItem(1008, 2, "items", "11x1110")
        >>> lst=CacheList(200)
        >>> lst
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> lst.put(content2, 'lru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> lst.put(content4, 'mru')
        'INSERTED: CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110'
        >>> lst.put(content5, 'mru')
        'INSERTED: CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110'
        >> lst.put(content3, 'lru')
        "INSERTED: CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> 1006 in lst
        True
        >>> contentExtra = ContentItem(1034, 2, "items", "other content")
        >>> lst.update(1008, contentExtra)
        'UPDATED: CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content'
        >>> lst
        REMAINING SPACE:170
        ITEMS:3
        LIST:
        [CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        >>> lst.clear()
        'Cleared cache!'
        >>> lst
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
   
    '''
    
    def __init__(self, size):
        self.head = None
        self.maxSize = size
        self.remainingSpace = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return 'REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}'.format(self.remainingSpace, self.numItems, listString)  

    __repr__=__str__

    def __len__(self):
        return self.numItems
   
   #Adds nodes to beginning of the list and evicts items
   #as necessary to free up space
    def put(self, content, evictionPolicy):
        #If less than max size, do not evict
        #If exceeds max size, evict according to eviction policy
        #If contend iD exists in list before insertion, move content to the beginning of list
        if content.cid in self:
            return f'Content {content.cid} already in cache, insertion not allowed'
        if content.size > self.maxSize:
            return 'Insertion not allowed'
        #If the content size is larger than the amount of space remaining, free up space until it can
        while content.size > self.remainingSpace:
            if (evictionPolicy == 'lru'):
                self.lruEvict()
            else:
                self.mruEvict()
        #Create a new node, update size remaining and make it the new head
        newNode = Node(content)
        self.remainingSpace -= content.size
        self.numItems += 1
        newNode.next = self.head
        self.head = newNode
        return f'INSERTED: {content}'
        
    
    #Finds an item from list by id
    #Moves item to the front of the list if found
    #Overload of the in function
    def __contains__(self, cid):
        #If size == 0, return False
        #If size == 1, return self.head.cid == cid
        if (self.numItems <= 1):
            return self.head and self.head.value.cid == cid
        
        prevItem = None
        currItem = self.head
        #While the item is not found, iterate to the next item
        while (currItem and currItem.value.cid != cid):
            prevItem = currItem
            currItem = currItem.next

        #If the item was not found, return False
        if (currItem == None):
            return False
        #If the item is found, moves the item to the front
        if not (currItem is self.head):
            prevItem.next = currItem.next
            currItem.next = self.head
            self.head = currItem
        return True

    #Will update a node with the given cid. 
    #Will also move the node to the top regardless of whether it has been updated or not
    #If the node is not found or the content update exceeds size limits then will not be updated
    def update(self, cid, content):
        if (self.numItems <= 1):
            #If there is an element, and that element matches the id and the new change 
            #does not exceed the max size, update item
            if (self.head and self.head.value.cid == cid and (content.size - self.head.value.size) <= self.remainingSpace):
                self.head = content
                return f'UPDATED: {content}'
            else:
                return 'Cache miss!'
        #If the item was not found, then return Cache Miss
        if not (cid in self):
            return 'Cache miss!'
        #If the item was found but the new size exceeds space left
        if (content.size - self.head.value.size) > self.remainingSpace:
            return 'Cache miss!'
        #Update the space remaining
        self.remainingSpace -= (content.size - self.head.value.size)
        self.head.value = content
        return f'UPDATED: {content}'


    #Removes most recently used element (first element)
    def mruEvict(self):
        if (self.numItems <= 1):
            self.head = None
            self.remainingSpace = self.maxSize
            self.numItems = 0
            return
        #Updates the amount of space left
        self.remainingSpace += self.head.value.size 
        self.head = self.head.next
        self.numItems -= 1
    
    #Removes least recently used element (last element)
    #Takes O(n) time to execute as it has to get to the end of the list
    def lruEvict(self):
        if (self.numItems <= 1):
            self.head = None
            self.remainingSpace = self.maxSize
            self.numItems = 0
            return
        temp = self.head
        while (temp.next.next != None):
            temp = temp.next
        
        #Updates the amount of space
        self.remainingSpace += temp.next.value.size
        temp.next = None
        self.numItems -= 1

    #Removes all items from the list
    def clear(self):
        self.head = None
        self.remainingSpace = self.maxSize
        self.numItems = 0
        return f'Cleared cache!'

class Cache:
    """
        # An extended version available on Canvas. Make sure you pass this doctest first before running the extended version

        >>> cache = Cache()
        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
        >>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")

        >>> content4 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content5 = ContentItem(1001, 51, "Content-Type: 1", "110011")
        >>> content6 = ContentItem(1007, 155, "Content-Type: 1", "10011011")

        >>> content7 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content8 = ContentItem(1002, 14, "Content-Type: 2", "<html><h2>'PSU'</h2></html>")
        >>> content9 = ContentItem(1006, 170, "Content-Type: 2", "<html><button>'Click Me'</button></html>")

        >>> cache.insert(content1, 'lru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> cache.insert(content2, 'lru')
        'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
        >>> cache.insert(content3, 'lru')
        'Insertion not allowed'

        >>> cache.insert(content4, 'lru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> cache.insert(content5, 'lru')
        'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
        >>> cache.insert(content6, 'lru')
        'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'

        >>> cache.insert(content7, 'lru')
        "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
        >>> cache.insert(content8, 'lru')
        "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
        >>> cache.insert(content9, 'lru')
        "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
        >>> cache
        L1 CACHE:
        REMAINING SPACE:177
        ITEMS:2
        LIST:
        [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        L2 CACHE:
        REMAINING SPACE:45
        ITEMS:1
        LIST:
        [CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011]
        <BLANKLINE>
        L3 CACHE:
        REMAINING SPACE:16
        ITEMS:2
        LIST:
        [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
        [CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>]
        <BLANKLINE>
        <BLANKLINE>
    """

    def __init__(self):
        self.hierarchy = [CacheList(200), CacheList(200), CacheList(200)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__


    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    #Inserts an item ito the Cache 
    def insert(self, content, evictionPolicy):
        return self.hierarchy[hash(content)].put(content, evictionPolicy)

    #Retrieves an item from the Cache, searches using content id
    def __getitem__(self, content):
        if (content.cid in self.hierarchy[hash(content)]):
            return self.hierarchy[hash(content)].head.value
        return 'Cache miss!'

    #Updates a given item in the Cache
    #Uses the content id given to search for the item
    def updateContent(self, content):
        if (self.hierarchy[hash(content)].update(content.cid, content) == 'Cache miss!'):
            return 'Cache miss!'
        return f'UPDATED: {self.hierarchy[hash(content)].head.value}'

if __name__=='__main__': 
    import doctest
    doctest.testmod()
    #doctest.run_docstring_examples(CacheList, globals(), name='HW5', verbose=True)
    #doctest.testfile('HW5_EXTENDED DOCTEST.py')

