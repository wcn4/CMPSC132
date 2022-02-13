# LAB2
# Due Date: 09/17/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random
import math

class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''
    #Sets initial values of stockDict, balance, and isStocked
    def __init__(self):
        #Key is id of item. Value is list containing [price, num remaining]
        self._stockDict = {156: [1.5, 3], 254: [2.0,3], 384: [2.5,3], 879: [3.0, 3] }
        #Starts with zero money
        self._balance = 0
        #Starts off stocked.
        self._isStocked = True


    #Will purchase item if possible. Returns any excess money
    #Returns a string, either with error or completion message
    def purchase(self, item, qty=1):
        if not (item in self._stockDict.keys()):
            return "Invalid item"
        if not self.isStocked:
            return "Machine out of stock"
        if self._stockDict[item][1] == 0:
            return "Item out of stock"
        if self._stockDict[item][1] < qty:
            return f'Current {item} stock: {self._stockDict[item][1]}, try again'
        cost = qty * self._stockDict[item][0]
        if (self._balance < cost):
            return f'Please deposit ${cost-self._balance}'
        
        self._balance -= cost
        self._stockDict[item][1] -= qty
        self._checkStock()
        
        if (self._balance == 0):
            return 'Item dispensed'
        change = self._balance
        self._balance = 0
        return f'Item dispensed, take your ${change} back' 


    #Inserts money into vending machine if it is stocked
    #Otherwise does not insert and returns error message
    def deposit(self, amount):
        if not self.isStocked:
            return f'Machine out of stock. Take your ${amount} back'
            
        if (amount >= 0):
            self._balance += amount
         
        if (isinstance(self._balance, int) or self._balance.is_integer()):
            return f'Balance: ${int(self._balance)}' 
        return f'Balance: ${self._balance}'

    #Increments the value of an item's stock if possible
    def _restock(self, item, stock):
        if not (item in self._stockDict.keys()):
            return "Invalid item"
        if (stock >= 0):
            self._stockDict[item][1] += stock
        return f'Current item stock: {self._stockDict[item][1]}'

    #Returns a boolean if any items are stocked.
    @property
    def isStocked(self):
        return self._isStocked
    
    #Returns a dictionary representing the vending stock
    @property
    def getStock(self):
        self._checkStock()
        return self._stockDict
    
    #Checks if there are items in stock, updates self._isStocked, returns none
    def _checkStock(self):
        for item in self._stockDict:
            if (self._stockDict[item][1] != 0):
                self._isStocked = True
                return
        self._isStocked = False
        return
    
    #Clears balance and returns string
    def cancelTransaction(self):
        if (self._balance == 0):
            return None
        change = self._balance
        self._balance = 0
        if (isinstance(change, int)):
            return f'Take your ${int(change)} back'
        return f'Take your ${change} back'

class Point2D:
    #Creates x and y values
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Checks if two points are equal if the values are equal
    def __eq__(self, other):
        if isinstance(other, Point2D):
            return (self.x == other.x) and (self.y == other.y)
        return False

    #Scales point coordinates by other factor
    def __mul__(self, other):
        if isinstance(other, int):
            return Point2D(self.x * other, self.y * other)
        return None

    #Calls __mul__ because of commutative property
    def __rmul__(self, other):
        if isinstance(other,int):
            return self * other
        return None


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    #Initializes line by creating points and delta values
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self._deltaX = self.point2.x - self.point1.x
        self._deltaY = self.point2.y - self.point1.y

    #Returns distance between two points
    @property
    def getDistance(self):    
        return round(math.sqrt(self._deltaX**2 + self._deltaY**2),3)
       
    #Returns constant rate of change of line
    @property 
    def getSlope(self): 
        if (self._deltaX == 0):
            return float('inf')
        return round(self._deltaY/self._deltaX, 3)


    #Returns y = mx+b of line unless m is undefined
    def _equation(self):
        if self._deltaX == 0:
            return 'Undefined'
        if self._deltaY == 0:
            return f'y = {round(self.point1.y - (self.getSlope * self.point1.x), 3)}' 
        return f'y = {self.getSlope}x + {round(self.point1.y - (self.getSlope * self.point1.x), 3)}'

    #Gets str representation
    def __str__(self):
        return self._equation()

    #Gets str representation
    def __repr__(self):
        return self._equation()

    #Checks if they are equal by seeing if two sets of points are equual
    #Does not take into account for whether order is swapped in other
    def __eq__(self, other):
        if isinstance(other, Line):
            return ((self.point1 == other.point1) and (self.point2 == other.point2))
        return False

    #Creates a new line where each point is scaled up by factor other
    def __mul__(self, other):
        if isinstance(other, int):
            return Line(self.point1 * other, self.point2 * other)
        return None
    
    #Calls regular __mul__ because of commutative property
    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other
        return None       

if __name__ == "__main__":
    import doctest
    #doctest.testfile('VendorTest.txt')
    doctest.testmod()
    #doctest.run_docstring_examples(Vendor, globals(), name='LAB2', verbose = True)

