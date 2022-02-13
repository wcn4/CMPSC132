# HW3
# Due Date: 10/15/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    #Returns a boolean depending on whether the stack is empty or not
    def isEmpty(self):
        return not bool(self.top)
        
    def __len__(self): 
        i = 0
        temp = self.top
        while (temp):
            i += 1
            temp = temp.next
        return i

    #Adds a new node to the top of the stack
    #Updates self.top
    def push(self,value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
     
    #Removes topmost node and returns its value
    #self.top is the node below it
    def pop(self):
        if self.isEmpty():
            return
        value = self.top.value
        self.top = self.top.next
        return value

    #Returns value of topmost node without altering the stack
    def peek(self):
        if self.isEmpty():
            return
        return self.top.value

#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    #Takes a string and determines if it is a valid number or not
    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
            >>> x._isNumber('5%')
            False
            >>> x._isNumber('(5)')
            False
        '''
        try: 
            float(txt)
            return True
        except:
            return False
        return False


    #Takes an infix expression (operator operand operator)
    #and converts it to (operator operator operand)
    #Postfix has no parentheses as it is not necessary
    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')

            >>> x._getPostfix('3 * ( ( ( 10 - 2 * 3 ) ) )')
            '3.0 10.0 2.0 3.0 * - *'
        '''
        
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        postfix = []
        #All tokens in the string
        tokens = txt.split()
        operators = ['+','-','*','/','^','(',')'] #List containing all operators
        
        #Checks if the first and last tokens are operators. If so, then it is not a valid expression
        if (len(tokens) > 0):
            if (tokens[0] in operators[:-2] or tokens[len(tokens)-1] in operators[:-2]):
                return

        #Scan through once to make sure it is a valid expression
        for count, item in enumerate(tokens):
            #If it is not a valid token
            if (not self._isNumber(item)) and (item not in operators):
                return

            if (count > 0):
                last = tokens[count-1]
                #If two operands are next to each other, there is a missing operator
                #Or if there was an attempt at implicit multiplication e.g. ) 5
                if self._isNumber(item) and (self._isNumber(last) or last == ')'):
                    return
                #If two non parenthesis operators are next to each other, it is illegal
                if item in operators[:-2] and last in operators[:-2]:
                    return
                #If there is an attempt at implicit multiplication such as e.g. 5 ( or ) (
                if item == '(' and (self._isNumber(last) or last == ')'):
                    return
                
            #Add left parentheses to stack
            if item == '(':
                #If there was an attempt at implicit multiplication
                if (count > 0 and self._isNumber(tokens[count-1])):
                    return
                postfixStack.push('(')
            
            if item == ')':
                #If there is a mismatched right parentheses
                if postfixStack.isEmpty():
                    return
                postfixStack.pop()

        #If there were any mismatched left parentheses
        if not postfixStack.isEmpty():
            return
        
        #The following are methods for what to do for each operator when encountered in a stack

        #Adds left Parentheses to stack
        def leftParen(operator):
            postfixStack.push(operator)

        #Adds all operators to postfix until it reaches a left parentheses or until the stack is empty
        def rightParen(operator):
            value = postfixStack.pop()
            while (value != '(' and not postfixStack.isEmpty()):
                #print(f'Value is {value}')
                postfix.append(value)
                value = postfixStack.pop()

        #Regular operator is the default case in which operators from the stack are appended until they are
        #above an element of lower precedence
            #leqPrecedence is a list of all operators with precedence less than or equal to the
            #precedence of the operator. The first two elements are of equal precedence
        def regularOperator(operator, leqPrecedence): 
            #While there is a higher order precedence operator
            while (not postfixStack.isEmpty() and postfixStack.peek() not in leqPrecedence):
                postfix.append(postfixStack.pop()) #pop it and add to the postfix expression
            if postfixStack.isEmpty() or postfixStack.peek()  == '(':
                postfixStack.push(operator)
                return
            #If they are of equal precedence, then the one in the stack gets appended
            if postfixStack.peek() in leqPrecedence[:2]:
                postfix.append(postfixStack.pop())
            postfixStack.push(operator)


        #Higher precedence operators are *,/,^
        def addsubtract(operator):
            regularOperator(operator, ['+','-','('])

        #Higher precedence operator is ^
        def multiplydivide(operator):
            regularOperator(operator, ['*','/','+','-','(',])

        #No higher precedence than ^ besides ()
        def exponent(operator):
            postfixStack.push(operator)
        
        #Mapping the functions above to their assigned operators
        operations = { '(':leftParen, ')':rightParen, '+':addsubtract, '-':addsubtract, '*':multiplydivide, '/':multiplydivide, '^':exponent }
        
        #For each item in tokens, append the number or do the corresponding action with each operator
        for item in tokens:
            if self._isNumber(item):
                postfix.append(str(float(item)))
            else:
                operations[item](item)

        #If there are any operators that remain in the stack, add them to the expression
        while not postfixStack.isEmpty():
            postfix.append(postfixStack.pop())

        #Join the postfix into one string
        return ' '.join(postfix)





    @property
    def calculate(self):
        '''`
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        #Converts the expression to postfix for evaluation
        postfix = self._getPostfix(self.getExpr)
        #If it cannot be successfully converted to postfix, then will return None
        if not postfix:
            return
        tokens = postfix.split()
        #Assigns each operator with their corresponding operation
        operations = { 
            '+':(lambda a,b: a+b),
            '-':(lambda a,b: a-b),
            '*':(lambda a,b: a*b),
            '/':(lambda a,b: a/b),
            '^':(lambda a,b: a**b)
            }
        #If there is no expression
        if len(tokens) == 0:
            return
        #For each token, add it to the stack if it is a number
        #If it is an operator, pop 2 elements from the stack, do the operation, and push result back to stack
        for item in tokens:
            if self._isNumber(item):
                calcStack.push(item)
            else:

                b = float(calcStack.pop())
                a = float(calcStack.pop())
                calcStack.push(operations[item](a,b))
        #When all is done, result should be at the top
        return float(calcStack.pop())

#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    #Determines if a word is a valid variable name or not
    #If it has a number at the start, it is not a valid variable name
    #If it is not alphanumeric, it is not a valid variable name
    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        if not word[0].isalpha():
            return False
        return word.isalnum() 

    #Replaces all instances of a stored variable in an expression with its actual value
    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        tokens = expr.split() 
        operators = ['+','-','*','/','^','(',')']
        calcObj = Calculator() 
        #For every token in the expression
        for i in range(len(tokens)):
            #If it is not a number or an operator
            if not calcObj._isNumber(tokens[i]) and tokens[i] not in operators:
                #Check if it a valid variable, if it is: replace it, if not: return nothing.
                if tokens[i] in self.states.keys():
                    tokens[i] = str(self.states[tokens[i]])
                else:
                    return
        #Return the replaced values
        return ' '.join(tokens)

            
    #Takes the expressions stored in self.expressions and calculates their values
    def calculateExpressions(self):
        self.states = {}
        self.progression = {}
        calcObj = Calculator()     # method must use calcObj to compute each expression
        #Splits the lines based off of semicolons
        lines = self.expressions.split(';')
        #For each line in the expression
        for count,line in enumerate(lines):
            tokens = line.split()
            #If the first token is a return value, return a value in the form '_return_ : value'
            if tokens[0] == 'return':
                expression = self._replaceVariables(' '.join(tokens[1:]))
                calcObj.setExpr(expression)
                self.progression['_return_'] = calcObj.calculate
                return self.progression

            #If it is not a valid variable name
            if not self._isVariable(tokens[0]): 
                self.states = {}
                return 

            #Otherwise, add an entry to self.progression of the form ' line : self.states'
            expression = self._replaceVariables(' '.join(tokens[2:]))
            calcObj.setExpr(expression)
            self.states[tokens[0]] = calcObj.calculate
            self.progression[line] = self.states.copy()
        return self.progression


if __name__ =='__main__':
    import doctest
    doctest.testmod()
    #doctest.run_docstring_examples(AdvancedCalculator, globals(), name='HW3', verbose=True)

