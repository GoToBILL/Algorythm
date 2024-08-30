import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())

def dfs(x):
    global res
    for go in lists[x]:
        if visited[go] == 0:
            if visited[x] == 1:
                visited[go] = 2
            else:
                visited[go] = 1
            dfs(go)
        else:
            if visited[go] == visited[x]:
                res = 0
            
            
        

for i in range(n):
    v,e = map(int,input().split())
    visited = [0 for _ in range(v+1)]
    lists = [[] for _ in range(v+1)]
    res = 1
    
    for j in range(e):
        a,b = map(int,input().split())
        lists[a].append(b)
        lists[b].append(a)
    
    for i in range(1,v+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i) 
    print("YES" if res else "NO")


