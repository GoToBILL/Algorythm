import sys
from collections import deque
a = int(sys.stdin.readline())
for k in range(a):
    N = int(sys.stdin.readline())
    res = [1,1,1,2,2,3]+[0]*(N)
    for i in range(5,N+1):
        res[i+1] = res[i]+res[i-4]
    print(res[N-1]) 
