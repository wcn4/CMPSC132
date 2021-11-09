class Queue:
    '''
        Python list implementation of a FIFO Queue
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


class Graph:
    '''
        >>> g1 = {'B': ['E', 'C'],
        ...       'F': [],
        ...       'C': ['F'],
        ...       'A': ['D', 'B'],
        ...       'D': ['C'],
        ...       'E': ['F']}
        >>> g = Graph(g1)
        >>> g.bfs('A')
        ['A', 'B', 'D', 'C', 'E', 'F']

        >>> g2 = {'Bran': ['East', 'Cap'],
        ...       'Flor': [],
        ...       'Cap':  ['Flor'],
        ...       'Apr':  ['Dec', 'Bran'],
        ...       'Dec':  ['Cap'],
        ...       'East': ['Flor']}
        >>> g = Graph(g2)
        >>> g.bfs('Apr')
        ['Apr', 'Bran', 'Dec', 'Cap', 'East', 'Flor']
    '''
    def __init__(self, graph_repr):
        self.adjacency_list = graph_repr

    def bfs(self, start):
        bfsList = []
        Q = Queue()
        Q.enqueue(start)
        #We will say that we visited the start position
        bfsList.append(start)
        while not Q.isEmpty():
            node = Q.dequeue()
            #Sort it so it is consistent
            self.adjacency_list[node].sort()
            #Given a string for the node
            #Must go to graph_repr to get the neighbors of that node
            for neighbor in self.adjacency_list[node]:
                #If this node has not been visited yet
                if neighbor not in bfsList:
                    #Add it to the list of visited nodes and enqueue it to get its neighbors
                    bfsList.append(neighbor)
                    Q.enqueue(neighbor)
        return bfsList


def run_doctest():
    import doctest
    doctest.testmod(verbose=True)

