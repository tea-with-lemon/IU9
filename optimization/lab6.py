import numpy as np
from numpy.linalg import inv


def  simplexHelper(t) :
    h, w = t[1].shape
    k, res = simplex(get_table(t[1], t[0], t[2]), w)
    H = np.delete(res[0], res[1], 1)
    k, (W, basis) = simplex(H[:-1, :], w - h)
    return  basis  if k != 0 else res[1], W[:-1,-1],-W[-1 ,-1]

def simplex(A,  offs, k=10):
    h , w = A. shape
    notbasis, basis = list(range (0, offs)), list(range(offs,  w-1))
    eqcount = w - offs - 1
    equations = list(range(eqcount))
    indices = np.arange(w)
    iters = 0
    for i in range(k):
        N = A[np.ix_([* equations], [* notbasis])]
        cb = A[np.ix_([h-1], [* basis] )]
        cn = A[np.ix_([h-1], [* notbasis])]
        iB = inv(A[np.ix_([* equations], [* basis])])
        d = np.dot(np.dot(cb, iB), N) - cn
        col = np.item(np.argmin(d))
        if [0, col] >= 0. :
            iters = i
            break
        alpha = np.dot(iB, N[:, col])
        posalpha = np.argwhere(alpha>0)
        beta = np.dot(iB, A[:eqcount], -1)
        balpha = beta[posalpha] / alpha[posalpha]
        pi = np.argmin(balpha).item()
        row = posalpha[pi].item()
        A[row, :] = np.divide(A[row, :], alpha[row])
        for j in range(h):
            if j == row:
                continue
            A[j] -= A[row]*A[j][col]
        A[:, [col, row + offs]] = A[:, [row + offs, col]]
        indices[[col, row + offs]] = indices[[row + offs, col]]
    return iters, (A, indices[basis])

'''
x = downhill(F,xStart,side,tol=1.0e-6)
    Downhill simplex method for minimizing the user-supplied
    scalar function F(x) with respect to the vector x.
    xStart = starting vector x.
    side   = side length of the starting simplex (default is 0.1)
from numpy import zeros,dot,argmax,argmin,sum
from math import sqrt
 
def downhill(F,xStart,side=0.1,tol=1.0e-6):
    n = len(xStart)                 # Number of variables
    x = zeros((n+1,n)) 
    f = zeros(n+1)
 
  # Generate starting simplex
    x[0] = xStart
    for i in range(1,n+1):
        x[i] = xStart
        x[i,i-1] = xStart[i-1] + side        
  # Compute values of F at the vertices of the simplex     
    for i in range(n+1): f[i] = F(x[i])
 
  # Main loop
    for k in range(500):
      # Find highest and lowest vertices
        iLo = argmin(f)
        iHi = argmax(f)       
      # Compute the move vector d
        d = (-(n+1)*x[iHi] + sum(x,axis=0))/n
      # Check for convergence
        if sqrt(dot(d,d)/n) < tol: return x[iLo]
 
      # Try reflection
        xNew = x[iHi] + 2.0*d              
        fNew = F(xNew)        
        if fNew <= f[iLo]:        # Accept reflection 
            x[iHi] = xNew
            f[iHi] = fNew
          # Try expanding the reflection
            xNew = x[iHi] + d               
            fNew = F(xNew)
            if fNew <= f[iLo]:    # Accept expansion
                x[iHi] = xNew
                f[iHi] = fNew
        else:
          # Try reflection again
            if fNew <= f[iHi]:    # Accept reflection
                x[iHi] = xNew
                f[iHi] = fNew
            else:
              # Try contraction
                xNew = x[iHi] + 0.5*d
                fNew = F(xNew)
                if fNew <= f[iHi]: # Accept contraction
                    x[iHi] = xNew
                    f[iHi] = fNew
                else:
                  # Use shrinkage
                    for i in range(len(x)):
                        if i != iLo:
                            x[i] = (x[i] - x[iLo])*0.5
                            f[i] = F(x[i])
    print "Too many iterations in downhill"
    print "Last values of x were"
    return x[iLo]
'''