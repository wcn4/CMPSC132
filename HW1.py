# HW1
# Due Date: 09/10/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import math

def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #Using the quadratic formula after deriving quadratic equation
	#from p = 2w+2h and A = wh, longer is the longer of the two sides
	#returned from the equation
    longer = ( (perimeter/2) + math.sqrt( (perimeter/2)**2 - 4*area) ) / 2
    if float.is_integer(longer) and float.is_integer(area/longer):
        return int(longer)
    return False

def frequency(aString):
    """
    >>> frequency('mama')
    ('consonant', {'m': 2, 'a': 2})
    >>> answer = frequency('We ARE Penn State!!!')
    >>> answer[0]
    'vowel'
    >>> answer[1]
    {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
    >>> frequency('One who IS being Trained')
    ('consonant', {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1})
    """
    #Dictionary containing all the letters that appear
    letters = {}
    aString = aString.lower()
	#Count all the occurances of each letter in the dictionary
    for letter in list(aString):
        if letter.isalpha():
            if not (letter in letters.keys()):
                letters[letter] = 0
            letters[letter] += 1
	#Determine whether the most
    mostFrequent = aString[0]
    for letter in letters.keys():
        if letters[letter] > letters[mostFrequent]:
            mostFrequent = letter
    if mostFrequent in {'a','e','i','o','u'}:
        mostFrequent = "vowel"
    else:
        mostFrequent = "consonant"
    return (mostFrequent, letters)

def successors(file):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """

    with open(file) as f: 
        contents = f.read()
	
	#Removes Line breaks and then joins it back together
    contents = contents.splitlines()
    contents = ''.join(contents)
    
	#Split the words based off of spaces and punctuation
    words = []
    for letter in list(contents):
        if letter in {' ',',','.','!','?',':',';'}:
		    #Put new words in after the split
            splitContent = contents.split(letter, 1) #Only allow one split at a time
            words.append(splitContent[0]) 
            if not letter == ' ':
                words.append(letter)
            contents = splitContent[1]
    
	#Generate word dictionary 
    wordDict = {}
    wordDict['.'] = []
    for i in range(len(words)-1):
        wordDict[words[i]] = []
    
	#Add the successors if they are not yet added
    wordDict['.'].append(words[0])
    for i in range(len(words)-1):
        if not (words[i+1] in wordDict[words[i]]): 
            wordDict[words[i]].append(words[i+1]) 
    return wordDict

def getPosition(num, digit):
    """
        >>> getPosition(1495, 5)
        1
        >>> getPosition(1495, 1)
        4
        >>> getPosition(1495423, 4)
        3
        >>> getPosition(1495, 7)
        False
    """
    #Okay to use recursion since ints have a limit within stack
    if (num % 10 == digit):
        return 1
	#If num is not in there
    if (num == 0):
        return False
	#Have to do this to ensure false values are not converted to ints implicitly
    x = getPosition(num//10, digit)
    if x:
        return x + 1
    return x


def hailstone(n):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #Will use iteration since upperbound is unknown (because of Collatz Conjecture)
    nums = []
	#Run the sequence until it hits one
    while(n != 1):
        nums.append(n)
        if(n%2==0):
            n = int(n/2)
        else:
            n = int(3*n+1)
    nums.append(1)
    return nums


def largeFactor(num):
    """
    >>> largeFactor(15)
    5
    >>> largeFactor(80)
    40
    >>> largeFactor(13)
    1
    """
	#Check factors from 2 to sqrt(num)
	#The first valid quotient will be the biggest
	#unless it is prime
    for i in range(2, int(math.sqrt(num))+1):
        if (num/i).is_integer():
            return int(num/i)
    return 1






#  To run doctes per function, uncomment the next three lines
#  and replace the word rectangle for the function name you want to test

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(largeFactor, globals(), name='HW1',verbose=True)
