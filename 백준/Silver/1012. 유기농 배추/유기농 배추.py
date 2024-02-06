import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(a,b):
    lists[a][b] = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < sero and 0 <= ny < garo and lists[nx][ny] == 1:
            dfs(nx,ny)
            
input = sys.stdin.readline
n = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(n):
    garo,sero,bachu = map(int,input().split())
    lists = [[0 for _ in range(garo)] for _ in range(sero)]
    
    for _ in range(bachu):
        x,y = map(int,input().split())
        lists[y][x] = 1
    
    res = 0
    for i in range(sero):
        for j in range(garo):
            if lists[i][j] == 1:
                # dfs
                dfs(i,j)
                res += 1
    print(res)