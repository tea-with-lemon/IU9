def Razl(n):
    d=2
    array=[]
    stop=n//2
    while (n!=1) and (d <= stop):
        while n%d==0:
            n=n/d
            array.append(d)
        else:
            d+=1
    return array

def Stroitel(n):
    global array
    for elem in array:
        if n%elem==0:
            print(n,"--",n//elem)
            Stroitel(n//elem)

n=int(input())
array=set(Razl(n))
print("strict graph {\n")
Stroitel(n)
print("\n}")
