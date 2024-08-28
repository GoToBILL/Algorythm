import sys

input = sys.stdin.readline

n,p,q = map(int,input().split())
dic = dict()
dic[0] = 1

def recursion(n):
    if n in dic:
        return dic[n]
    dic[n] = recursion(n // p) + recursion(n // q)
    return dic[n]

print(recursion(n))
