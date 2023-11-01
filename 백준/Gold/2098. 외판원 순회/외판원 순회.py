
import sys
from collections import deque
import heapq
def count(route,N):
    cnt = 0
    for i in range(1,N):
        if route & (1 << (i-1)) != 0:
            cnt += 1
    return cnt
def isin(x,route):
    if route & (1 << (x-1)) != 0:
        return True
    return False
def min_value(k,route,N,lists,dp):
    MIN = inf
    for i in range(1,N):
        if isin(i,route):
            before_route = route & ~(1 << (i-1))
            res = lists[k][i] + dp[i][before_route]
            if res < MIN:
                MIN = res
    return MIN
def solution(N,lists,dp):
    for i in range(N):
        for j in range(N):
            if not lists[i][j]:
                lists[i][j] = inf
    for i in range(1,N):
        dp[i][0] = lists[i][0]
    
    for i in range(1,N-1):
        for route in range(1,size):
            if i == count(route,N):
                for k in range(1,N):
                    if not isin(k,route):
                        dp[k][route] = min_value(k,route,N,lists,dp)
    dp[0][size-1] = min_value(0,size-1,N,lists,dp)
    return dp[0][size-1]

N = int(sys.stdin.readline())
size = 2**(N-1)
inf = sys.maxsize
dp = [[inf]*size for _ in range(N)]
lists = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

print(solution(N,lists,dp))