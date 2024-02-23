import heapq

def solution(N, road, K):
    answer = 0
    inf = int(1e9)
    lists = [[] for _ in range(N+1)]
    
    for i in range(len(road)):
        lists[road[i][0]].append([road[i][1],road[i][2]])
        lists[road[i][1]].append([road[i][0],road[i][2]])
    distance = [inf for _ in range(N+1)]
    distance[1] = 0
    hq = []
    heapq.heappush(hq,[0,1])
    while hq:
        out = heapq.heappop(hq)
        if out[0] > distance[out[1]]:
            continue
        for x,cost in lists[out[1]]:
            new_cost = out[0] + cost
            if new_cost < distance[x]:
                distance[x] = new_cost
                heapq.heappush(hq,[new_cost,x])
    return len(list(filter(lambda x: x <= K,distance[1:])))