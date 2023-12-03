
import sys
from collections import deque
import heapq
def bellman(start):
    distance = [inf]*(point+1)
    distance[start] = 0
    for i in range(point):
        for s,e,v in graph:
            if distance[e] > distance[s]+v:
                if i == point-1:
                    return True
                distance[e] = distance[s]+v
    return False
n = int(sys.stdin.readline())
for _ in range(n):
    point,cnt_graph,warm = map(int,sys.stdin.readline().split())
    graph = []
    res = [[0]*(point+1) for _ in range(point+1)]

    for j in range(cnt_graph):
        a,b,c = map(int,sys.stdin.readline().split())
     
        graph.append((a,b,c))
        graph.append((b,a,c))
    for t in range(warm):
        a,b,c = map(int,sys.stdin.readline().split())
        graph.append((a,b,-c))
    inf = int(1e9)
    if bellman(1):
        print("YES")
    else:
        print("NO")

    