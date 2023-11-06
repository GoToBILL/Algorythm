import sys
from collections import deque        

input = sys.stdin.readline

n,m = map(int, input().split())
tree = {i : [] for i in range(1, n+1)}

for _ in range(n -1):
    a,b,k = map(int ,input().split())
    tree[a].append([b,k])
    tree[b].append([a,k])

for _ in range(m):
    a,b = map(int ,input().split())
    sum = 0
    
    dq = deque()
    ind = [0 for _ in range(n)]
    ind[a-1] = 1
    for definition,value in tree[a]:
        ind[definition - 1] = 1
        dq.append([definition,value])
    while dq:
        pop_ele = dq.popleft()
        if pop_ele[0] == b:
            print(pop_ele[1])
            break
        for x,y in tree[pop_ele[0]]:
            if ind[x-1] == 0:
                ind[x-1] = 1
                dq.append([x,y + pop_ele[1]])