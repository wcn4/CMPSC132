# LAB3
# Due Date: 10/01/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.
#        All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given


#Gets the count of a certain item within a list
def get_count(aList, item):
    '''
        >>> get_count([1,4,3.5,'1',3.5, 9, 1, 4, 2], 1)
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 3.5)  
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 9)   
        1
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 'a') 
        0
    '''
    #If the list has nothing, there are no instances of that object within the list
    if (len(aList)==0):
        return 0
    #Otherwise, add all the previous instances of the item with a 1 if
    #the last object is the item, a 0 if it isn't. 
    #Some typecasting tricks may have been used
    return get_count(aList[:-1], item) + int(aList[-1] == item)

#Replaces all instances of an item with a new item within a list
def replace(numList, old, new):
    '''
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    '''
    #If the list is empty, return a new empty list to build off of
    if (len(numList) == 0):
        return []
    #Is the last element an item to replace?
    if (numList[-1] == old):
        #If so, append the new item to the new list
        return replace(numList[:-1], old, new) + [new]
    #Otherwise, append the item unchanged to the new list
    return replace(numList[:-1], old, new) + [numList[-1]]

#Takes a possibily deeplist and flattens it into a 1D list
def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    #If the list is empty, return a new empty list to build off of
    if (len(aList) == 0):
        return []
    #If the last item is a list
    if (isinstance(aList[-1], list)):
        #Flatten the last item before appending it to the new flattened list
        return flat(aList[:-1]) + flat(aList[-1])
    #Append the item to the new flattened list
    return flat(aList[:-1]) + [aList[-1]]



def neighbor(n):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """
    #Error filtering?
    if n < 0:
        return -1
    #If it is a two digit number
    if n < 100:
        #Return 1 digit if they are the same, both if not
        if n//10 == n%10:
            return n%10
        return n
    #Get the new number for m-1 digits  without identical neighbors
    other = neighbor(n//10)
    #If the digit to append is the same as its neighbor, do not append.
    if (other%10 == n%10):
        return other
    #Append if it is not.
    return other*10 + (n%10)



if __name__=='__main__':
    import doctest
    doctest.testmod()     # Uncomment this line to run all docstrings
    #doctest.run_docstring_examples(get_count, globals(), name='LAB3',verbose=True)
