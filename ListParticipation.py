#Using list comprehension to produce [0,2,6,12,20,30,42,56,72,90]
a = [x**2 + x for x in range(0,10)]
print(a)

#Using list comprehension to produce lowercase alphabet list
alphabet = [chr(97+x) for x in range(0,26)]
print(alphabet)


#Modified Generator that still runs in O(sqrt(n)) time but lists factors in order
#Uses a stack to achieve the in order listing
def factors(n):
    k=1
    stack = []
    while k**2 < n:
        if n%k == 0:
            yield k
            stack.append(k)
        k+=1
    if k*k == n:
        yield k

    while (len(stack) != 0):
        yield int(n/stack.pop(-1))

#Tests?
print(list(factors(100)))
print(list(factors(12)))
print(list(factors(91)))
print(list(factors(20)))
print(list(factors(343)))
print(list(factors(25)))
