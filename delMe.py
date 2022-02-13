def canWin(n):
    if (n < 0):
        return False
    if (n <= 3):
        return True
    #Assuming opponent is smart and trying to win, if you are on a multiple of four, you are guaranteed to lose
    if (n % 4 == 0):
        return False
    #See if the opponent can win, and return the inverse of that
    return not canWin(n - (n%4))

print(canWin(1))
print(canWin(4))
print(canWin(5))
print(canWin(8))
print(canWin(9))
