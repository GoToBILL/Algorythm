import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(a):
    if a != ziphap[a]:
        ziphap[a] = find_parent(ziphap[a])
    return ziphap[a]

def union(a,b):
    a = find_parent(a) # a의 루트 노드 찾기
    b = find_parent(b) # b의 루트 노드 찾기

    if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
        return
    if a < b: # a와 b의 루트 노드가 다르면 두 집합을 합치기
        ziphap[b] = a
    else:
        ziphap[a] = b
n,m = map(int,input().split())
ziphap = [i for i in range(n+1)]

for i in range(m):
    standard,left,right = map(int,input().split())
    if standard == 0:
        union(left,right)
    else:
        if find_parent(right) == find_parent(left):
            print("YES")
        else:
            print("NO")
