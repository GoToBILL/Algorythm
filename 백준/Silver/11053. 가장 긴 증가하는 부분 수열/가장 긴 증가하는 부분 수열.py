import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
lists = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(0, i):
        if lists[i] > lists[j]:
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))