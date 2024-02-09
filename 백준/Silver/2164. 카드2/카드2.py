import sys
from collections import defaultdict, deque
import collections
import heapq as hq
n = int(sys.stdin.readline())
lists = list(range(1,n+1))
lists = deque(lists)
while len(lists)>1:
    lists.popleft()
    ex = lists.popleft()
    lists.append(ex)
print(lists[0])