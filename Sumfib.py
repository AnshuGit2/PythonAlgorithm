# python3
n = int(input())

dn = int (input())
def fib(n):
    a, b = 0, 1
    r = 1
    if n < 1:
        return 0
    for i in range(n - 1):
        a, b = b, (a + b)%10
        r += b
        r %= 10
    return r
print (fib(n))