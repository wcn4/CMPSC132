def quickSort(numList):
    '''
        >>> quickSort([3, 5, 4, 1, 2])
        [1, 2, 3, 4, 5]
        >>> quickSort([7,2,1])
        [1, 2, 7]
        >>> quickSort([1,1,1,1,1])
        [1, 1, 1, 1, 1]
        >>> quickSort([4,6,5,2,3])
        [2, 3, 4, 5, 6]
        >>> quickSort([4,6,5,2,3,3])
        [2, 3, 3, 4, 5, 6]
    '''
        #>>> quickSort([2,1,2,1,2,1])
        #[1, 1, 1, 2, 2, 2]
    n=len(numList)
    #By definition, a list of size one or zero will be sorted
    if n<=1:
        return numList
    #x is the pivot
    #left is set to same index as pivot
    #Right is set last index
    x, left, right = numList[0], 0, n-1
    while left<right:
        #If the left index is less than x, increment left by 1
        if numList[left]<=x:    
            left+=1
        else:
        #Otherwise, swap the left and right values
        #and then decrement the right by 1
            numList[left], numList[right]  =  numList[right], numList[left]
            right -=1
    #Once left and right are equal or right is less than left
    #Swap the pivot with the left value
    numList[0], numList[left] = numList[left], numList[0]
    #Recursively call quickSort on the left and right parts of the list
    quickSort(numList[:left])
    quickSort(numList[left+1:])
    return numList

def quickSort2(numList):
    '''
        >>> quickSort2([3, 5, 4, 1, 2])
        [1, 2, 3, 4, 5]
        >>> quickSort2([7,2,1])
        [1, 2, 7]
        >>> quickSort2([1,1,1,1,1])
        [1, 1, 1, 1, 1]
        >>> quickSort2([4,6,5,2,3])
        [2, 3, 4, 5, 6]
        >>> quickSort2([4,6,5,2,3,3])
        [2, 3, 3, 4, 5, 6]
        >>> quickSort2([2,1,2,1,2,1])
        [1, 1, 1, 2, 2, 2]
    '''
    return quickSort3(numList, 0, len(numList)-1)
    
def quickSort3(numList, l, r):
    n=r-l
    #By definition, a list of size one or zero will be sorted
    if n <= 1:
        return numList
    
    if n==2:
        if numList[1] < numList[0]:
            numList[0],numList[1] = numList[1],numList[0]
        return numList
    #x is the pivot
    #left is set to same index as pivot
    #Right is set last index
    x, left, right = numList[0], l+1, r
    while not (right < left):
        while left<=right and numList[left] <= x:
            print('\tMoving left var from ', numList[left], '(i=', left, ') to', left+1)
            left+=1
        while right >= left and numList[right] >= x: 
            print('\tMoving right var from ', numList[right], '(i=', right, ') to', right+1)
            right -=1
        if not right < left:
            numList[left], numList[right]  =  numList[right], numList[left]
        print('Left is ', left, ' Right is ', right, ' and max index is ', len(numList)-1)
    
    if (left >= len(numList)):
        left -= 1
    numList[0], numList[left] = numList[left], numList[0]
    print('\tSplitting into ', numList[:left], ' and ', numList[(left+1):], 'at ', left)
    quickSort3(numList, 0, left-1)
    quickSort3(numList, left+1, len(numList)-1)
    return numList


'''
  
        #Otherwise, swap the left and right values
        #and then decrement the right by 1
    #Once left and right are equal or right is less than left
    #Swap the pivot with the left value
    print("\tBefore final swap: ", numList[l:r], end=' after: ')
        if numList[left]<=x and left<=right:   
            print('\tIncrementing Left (Left = ', left, ') ',  numList[left], end=' ')
            left+=1
            print('\tNow Left is (Left = ', left, ') ',  numList[left])
        if numList[right]>=x and right>=left:
            print('\tDecrementing Right (Right = ', right, ') ',  numList[right], end=' ') 
            right-=1
            print('\tNow Right is (Right = ', right, ') ', numList[right])
        if numList[left] >= x and numList[right] <= x:
            print('\tSwapping ', numList[left], ' and ', numList[right], end=' ')
            numList[left], numList[right]  =  numList[right], numList[left] 
            print('\tNow list is ', numList[l:r])


    print('\t', numList[l:r])
    print('\tSplitting into ', numList[:left], ' and ', numList[left+1:], 'at ', left)
    #Recursively call quickSort on the left and right parts of the list
'''
