import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
lists = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

index = [[-1 for i in range(m)] for j in range(n)]

stack = deque()
for i in range(n):
    for j in range(m):
        if lists[i][j] == 2:
            stack.append([i,j])
            index[i][j] = 0
        elif lists[i][j] == 0:
            index[i][j] = 0




while stack:
    pop_ele = stack.popleft()

    for i in range(4):
        nx = pop_ele[0] + dx[i]
        ny = pop_ele[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m and index[nx][ny] == -1:
            if lists[nx][ny] == 1:
                stack.append([nx,ny])
                index[nx][ny] = index[pop_ele[0]][pop_ele[1]] + 1

for i in range(n):
    for j in range(m):
        print(index[i][j],end=" ")
    print()