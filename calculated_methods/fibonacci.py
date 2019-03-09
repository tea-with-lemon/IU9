# def fib(num):
#     a,b,flist=0,1,[]
#     while a<num:
#         flist.append(a)
#         a,b=b, a+b
#     return flist

def rec(a, b, num, flist):
    if a <= num:
        flist.append(a)
        return rec(b, a + b, num, flist)
    else:
        return flist

def fib(maxnum):
    a, b, flist = 0, 1, []
    return rec(a, b, maxnum, flist)

print(fib(5))