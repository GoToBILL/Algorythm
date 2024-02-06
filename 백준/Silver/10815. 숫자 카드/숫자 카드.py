import sys
from collections import deque
sys.setrecursionlimit(10**6)

def is_here(a):
    start = 0
    last = len(lists)-1
    while start <= last:
        mid = (start+last) // 2
        if lists[mid] > a:
            last = mid - 1
        elif lists[mid] < a:
            start = mid + 1
        else:
            return 1
    return 0

input = sys.stdin.readline
n = int(input())
lists = list(map(int,input().split()))
lists.sort()


m = int(input())
find_list = list(map(int,input().split()))

for num in find_list:
    if is_here(num):
        print(1,end=' ')
    else:
        print(0,end=' ')