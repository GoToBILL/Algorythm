import sys
from collections import deque
from itertools import permutations as pt
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n,m = map(int,input().split())
num_list = [i for i in range(1,n+1)]
for lists in pt(num_list,m):
    print(" ".join(map(str,lists)))