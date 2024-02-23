from collections import deque 
def solution(maps):
    answer = 0
    word = ["O","E","L","S"]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                start = [i,j]
            elif maps[i][j] == "L":
                laver = [i,j]
            elif maps[i][j] == "E":
                end = [i,j]
    dq = deque()
    dq.append(start)
    lists = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    sero = len(maps)
    garo = len(maps[0])
    lists[start[0]][start[1]] = 0
    flag = 0
    mid = 0
    while dq:
        out = dq.popleft()
        if out[0] == laver[0] and out[1] == laver[1]:
            mid = lists[laver[0]][laver[1]]
            flag= 1
            break
        for i in range(4):
            nx = out[0] + dx[i]
            ny = out[1] + dy[i]
            if 0 <= nx < sero and 0 <= ny <garo and lists[nx][ny] == -1 and maps[nx][ny] in word:
                dq.append([nx,ny])
                lists[nx][ny] = lists[out[0]][out[1]] + 1
    if flag == 0:
        return -1
    
    dq = deque()
    dq.append(laver)
    lists = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    lists[laver[0]][laver[1]] = 0
    while dq:
        out = dq.popleft()
        if out[0] == end[0] and out[1] == end[1]:
            mid += lists[end[0]][end[1]]
            flag = 2
            break
        for i in range(4):
            nx = out[0] + dx[i]
            ny = out[1] + dy[i]
            if 0 <= nx < sero and 0 <= ny <garo and lists[nx][ny] == -1 and maps[nx][ny] in word:
                dq.append([nx,ny])
                lists[nx][ny] = lists[out[0]][out[1]] + 1
                
    if flag != 2:
        return -1
    return mid