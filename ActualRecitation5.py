
def hailstone(n):
    if (n==1):
        return [1]
    return [n] + hailstone([n//2, 3*n + 1][n%2])

print(hailstone(1))
print(type(hailstone(1)))
print("Doing hailstone(10)")
print(hailstone(10))
