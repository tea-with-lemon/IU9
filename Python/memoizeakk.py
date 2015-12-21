import sys
sys.setrecursionlimit(10000)
def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return helper
@memoize
def A(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return A(m - 1, 1)
    if m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))

print(A(3, 2))