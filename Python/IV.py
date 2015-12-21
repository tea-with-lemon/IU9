class Iv:
    def __init__(self,*args):
        self.left=args[0]
        self.right=args[-1]
    def __add__(self, other):
        return(Iv(self.left+other.left, self.right+other.right))
    def __sub__(self, other):
        return(Iv(self.left-other.left, self.right-other.right))
    def __mul__(self, other):
        #Умножение: [a,b] × [c,d] = [min (ac, ad, bc, bd), max (ac, ad, bc, bd)]
        a=self.left
        b=self.right
        c=other.left
        d=other.right
        return(Iv(min(a*c, a*d, b*c, b*d), max(a*c, a*d, b*c,b*d)))
    def __truediv__(self,other):
        #Деление: [a,b] / [c,d] = [min (a/c, a/d, b/c, b/d), max (a/c, a/d, b/c, b/d)]
        a = self.left
        b = self.right
        c = other.left
        d = other.right        
        if c*d <= 0:
            raise ValueError('Интервал %s не может быть вычислен, потому что он содержит 0' % other)
        return (Iv(min(a/c, a/d, b/c, b/d),max(a/c, a/d, b/c, b/d)))
    def __str__(self):
            return '[%g, %g]' % (self.left, self.right)
        
print(Iv(9.5, 10.5) + Iv(5.75, 6.25))
print(Iv(9.5, 10.5) - Iv(5.75, 6.25))
print(Iv(9.5, 10.5) * Iv(2.0))
print(Iv(9.5, 10.5) / Iv(2.0))
print(Iv(9.5, 10.5) / Iv(-1.0, 1.0))



"""I = Iv
a = I(9.5, 10.5)
b = I(5.75, 6.25)
expr = 'a+b', 'a-b', 'a*b', 'a/b'
for e in expr:
    print ('%s =' % e, eval(e))"""

