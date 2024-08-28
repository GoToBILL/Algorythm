import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n,p,q,x,y = map(int,input().split())
dic = dict()
dic[0] = 1

def recursion(n):
    if n <= -1:
        return dic[0]
    if n in dic:
        return dic[n]
    dic[n] = recursion(n // p-x) + recursion(n // q-y)
    return dic[n]

print(recursion(n))
