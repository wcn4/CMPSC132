def hailstone(n):
    if (n==1):
        return [1]
    if (n%2 == 1):
        return [n] + hailstone(3*n+1)
    return [n] + hailstone(n//2)

print(hailstone(10))
print(hailstone(1))
print(hailstone(7))
