#Lab #0
#Due Date: 08/28/2021, 11:59PM

# More information on pass statement: 
#    https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement



def sumSquares(aList):
    """
        >>> sumSquares([1,5,-3,5.5,359,8,14,-25,1000])
        129171.25
        >>> sumSquares([1,5,-3,5,45.5,8.5,-5,500,6.7,-25])
        2187.39
        >>> sumSquares(['14',5,-3,5,9.0,8,14,7,'Hello'])
        390.0
        >>> sumSquares(5)
        >>> sumSquares('5') is None
        True
        >>> sumSquares(6.15)

    """
    sum = 0
    for x in range(len(aList)):
        print(pow(aList[x], 2))
        sum += pow(aList[x], 2)
    return sum
    pass   # remove this line before submitting

print(sumSquares([1,5,-3,5.5,359,8,14,-25,1000]))
print(sumSquares([1,5,-3,5,45.5,8.5,-5,500,6.7,-25]))
print(sumSquares([0,5,-3,5,9.0,8,14,7,0]))
print(sumSquares(5))
print(sumSquares('5'))
print(sumSquares(6.15))

## Uncomment next 3 lines if not running doctest in the command line
if __name__ == "__main__":
    import doctest
    doctest.testmod()
