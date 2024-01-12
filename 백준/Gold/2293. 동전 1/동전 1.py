import sys         
import heapq


input = sys.stdin.readline
n,k = map(int, input().split())
lists = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1
for num in lists:
    for i in range(num,k+1):
        if i - num >= 0:
            dp[i] += dp[i-num]
print(dp[k])