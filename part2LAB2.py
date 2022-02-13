# LAB2
# Due Date: 09/17/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return (self.x == other.x) and (self.y == other.y)
        return False

    def __mul__(self, other):
        if isinstance(other, int):
            return Point2D(self.x * other, self.y * other)
        return None

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
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.point1 = point1
        self.point2 = point2
        self._deltaX = self.point2.x - self.point1.x
        self._deltaY = self.point2.y - self.point1.y

    @property
    def getDistance(self):    
        return round(math.sqrt(self._deltaX**2 + self._deltaY**2),3)
       
    @property 
    def getSlope(self): 
        if (self._deltaX == 0):
            return float('inf')
        return round(self._deltaY/self._deltaX, 3)

    def _equation(self):
        if self._deltaX == 0:
            return 'Undefined'
        if self._deltaY == 0:
            return f'y = {round(self.point1.y - (self.getSlope * self.point1.x), 3)}' 
        return f'y = {self.getSlope}x + {round(self.point1.y - (self.getSlope * self.point1.x), 3)}'

    def __str__(self):
        return self._equation()

    def __repr__(self):
        return self._equation()

    def __eq__(self, other):
        if isinstance(other, Line):
            return ((self.point1 == other.point1) and (self.point2 == other.point2))
        return False

    def __mul__(self, other):
        if isinstance(other, int):
            return Line(self.point1 * other, self.point2 * other)
        return None

    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
