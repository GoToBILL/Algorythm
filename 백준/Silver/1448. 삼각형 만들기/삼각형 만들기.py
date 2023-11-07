import sys      

def res():
    for i in range(0,len(lists)-2):
        if lists[i] < lists[i+1] + lists[i+2]:
            print(sum(lists[i:i+3]))
            return
    print(-1)

input = sys.stdin.readline
n = int(input())
lists = [int(input()) for _ in range(n)]
lists.sort(reverse=True)
res()

