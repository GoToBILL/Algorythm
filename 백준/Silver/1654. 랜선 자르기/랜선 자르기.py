n,m = map(int, input().split())
lists = [int(input()) for i in range(n)]

MAX = max(lists)
l = 1
r = MAX
print_res = 1

while l <= r:
    mid = (l + r) // 2

    res = 0
    for pipe in lists:
        res += pipe // mid
    if res >= m:
        l = mid + 1
        print_res = mid
    else:
        r = mid - 1
print(print_res)