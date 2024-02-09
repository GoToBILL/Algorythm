import sys
from collections import deque
from collections import defaultdict
from itertools import permutations as pt
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
sys.setrecursionlimit(10**6)

def tree(x,SUM,total):
    global count
    if x == n:
        if SUM == m and total != 0:
            count += 1
        return
    tree(x+1,SUM + lists[x],total+1)
    tree(x+1,SUM,total)

input = sys.stdin.readline
n,m = map(int,input().split())

count = 0
lists = list(map(int,input().split()))
tree(0,0,0)
print(count)