import sys
from collections import deque
from itertools import permutations as pt
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n , m = map(int,input().split())

dp = [0] * (m)
dp.insert(0,1)
for i in range(n):
    a = int(input())
    for j in range(a,m+1):
        dp[j] += dp[j-a]

print(dp[m])

