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
dict = defaultdict(int)
for num in lists:
    dict[num] += 1
m = int(input())
want_find = list(map(int,input().split()))
print(" ".join(str(dict[x]) if x in dict else "0" for x in want_find))
