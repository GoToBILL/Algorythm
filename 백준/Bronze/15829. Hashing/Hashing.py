import sys      

input = sys.stdin.readline
n = int(input())
str_n = input()

res = 0

for i in range(n):
    res += (ord(str_n[i]) - 96) * (31 ** i)
print(res)