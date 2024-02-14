import collections
import heapq
import sys
import bisect as bs

n = int(sys.stdin.readline())
lists = list(map(int,sys.stdin.readline().split()))
dp = [0]*(n)
res = [-sys.maxsize]
for i,v in enumerate(lists):
    if v > res[-1]:
        dp[i] = len(res)-1
        res.append(v)
    else:
        dp[i] = bs.bisect_left(res,v)-1
        res[dp[i]+1] = v
MAX,anw = max(dp),[]
for i in range(n-1,-1,-1):
    if dp[i] == MAX:
        anw.append(lists[i])
        MAX -= 1
anw.reverse()
print(max(dp)+1)
print(*anw)