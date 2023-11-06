import sys      

input = sys.stdin.readline
n = int(input())
lists = [[-1 for _ in range(n+1)] for _ in range(n+1)]

a,b = map(int, input().split())
m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    lists[x][y] = 1
    lists[y][x] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if lists[i][j] == -1:
                if lists[i][k] != -1 and lists[k][j] != -1:
                    lists[i][j] = lists[i][k] + lists[k][j]
                    lists[j][i] = lists[i][k] + lists[k][j]
print(lists[a][b])
