import sys
from collections import deque
from collections import defaultdict
from itertools import permutations as pt
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
import bisect
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())
lists = list(map(int,input().split()))
lists.sort()
m = int(input())
want_find = list(map(int,input().split()))
for num in want_find:
    a = bisect.bisect_left(lists,num)
    if a != len(lists) and lists[a] == num:
        print(1,end=" ")
    else:
        print(0,end=" ")
