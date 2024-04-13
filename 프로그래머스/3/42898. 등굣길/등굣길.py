def solution(m, n, puddles):
    lists = [[0 for _ in range(m+1)] for _ in range(n+1)]
    DIVIDE = 1000000007
    
    lists[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles:
                lists[i][j] = 0
                continue
            if i == 1 and j == 1:
                continue
            lists[i][j] = lists[i-1][j] + lists[i][j-1]
    print(lists)
    return lists[n][m] % DIVIDE