import numpy as np
n=int(input())
m=int(input())
matrix=np.zeros((n,n))
for _ in range(m):
    x,y=map(int, input().split(' '))
    matrix[x][y]=1
    matrix[y][x]=1
print(matrix)
