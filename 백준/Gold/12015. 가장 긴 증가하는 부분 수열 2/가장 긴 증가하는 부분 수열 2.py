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
stack = [0]
for x in lists:
    if x > stack[-1]:
        stack.append(x)
    else:
        stack[bisect.bisect_left(stack,x)] = x
print(len(stack)-1)
