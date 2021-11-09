class Complex:

    def __init__(self,r,i):
        self._real = r
        self._imag = i

    def __str__(self):
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"
        else:
           return f"{self._real} - {abs(self._imag)}i"

    def conjugate(self):
        ans = Complex(self._real, -1*self._imag)
        return ans

    def __mul__(self,other):
        if isinstance(other, Complex):
            real_part = self._real*other._real-self._imag*other._imag
            imag_part = self._real*other._imag+self._imag*other._real
            ans = Complex(real_part, imag_part)
        else:
            ans = Complex(self._real*other, self._imag*other)
        return ans

    def __rmul__(self,other):
        return self * other


class Real(Complex):
    '''
    >>> x = Real(3)
    >>> y = Real(8) 
    >>> z = Complex(2, 5) 
    >>> op1 = x * y  
    >>> print(op1)
    24 + 0i
    >>> type(op1)
    <class '__main__.Real'>
    >>> op2 = x * 2 
    >>> print(op2) 
    6 + 0i
    >>> type(op2)   
    <class '__main__.Real'>
    >>> op3 = 2 * y 
    >>> print(op3) 
    16 + 0i
    >>> type(op3)   
    <class '__main__.Real'>
    >>> op4 = x * z 
    >>> print(op4) 
    6 + 15i
    >>> type(op4)   
    <class '__main__.Complex'>
    >>> x = Real(3) 
    >>> int(x) * [1,2,3] 
    [1, 2, 3, 1, 2, 3, 1, 2, 3]
    >>> y = int(x) 
    >>> y
    3
    >>> isinstance(y, int) 
    True
    >>> isinstance(y, Real) 
    False
    >>> z = float(x)        
    >>> z                   
    3.0
    >>> isinstance(z, float) 
    True
    >>> isinstance(z, Real)  
    False
    '''
    
    def __init__(self, value):
        super().__init__(value, 0)

    #Handles multiplicaton between Real and Real numbers, Real and Complex
    #and Real * int or Real * float
    #Delegates all other cases to complex value
    def __mul__(self, other):
        if isinstance(other, Real):
            return Real(self._real * other._real)
        elif isinstance(other, int) or isinstance(other, float):
            return Real(self._real * other)
        else:
            return super().__mul__(other) #Delegate all other cases to complex class

    def __rmul__(self, other):
        return self * other

    #If it is a real or complex class, compares coordinates to see if they are equal
    #Will return false in all other cases
    def __eq__(self, other):

        ''' Returns True if other is a Real object that has the same value or if other is
            a Complex object with _imag=0 and same value for _real, False otherwise

            >>> Real(4) == Real(4)
            True
            >>> Real(4) == Real(4.0)
            True
            >>> Real(5) == Complex(5, 0)
            True
            >>> Real(5) == Complex(5, 12)
            False
            >>> Real(5) == 5.5
            False
        '''
        # YOUR CODE STARTS HERE

        if isinstance(other, Real) or isinstance(other, Complex):
            return (self._real == other._real and self._imag == other._imag)
        else:
            return False

    #Converts real value to int
    def __int__(self):
        return int(self._real)

    #Converts real value to float
    def __float__(self):
        return float(self._real)

    
    
if __name__=='__main__':
    import doctest
    doctest.testmod()


