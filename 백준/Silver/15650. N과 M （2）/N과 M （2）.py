from os import spawnl
from re import split
import sys
from collections import defaultdict, deque
def dfs(x,gi):
    if x == m:
        for x in res:
            print(x,end=' ')
        print()
        return
    else:
        for i in range(gi+1,n+1):
                res.append(i)
                dfs(x+1,i)
                res.pop()
n,m = map(int,input().split())
res = []
dfs(0,0)