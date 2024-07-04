from collections import defaultdict as df

def solution(edges):
    answer = [0,0,0,0]
    def default_list():
        return [0, 0]

    graph = df(default_list)
    main_deg = 0
    for fro, to in edges:
        graph[fro][1] += 1
        graph[to][0] += 1
    
    for key,lists in graph.items():
        if lists[0] == 0 and lists[1] >= 2:
            answer[0] = key
            main_deg = key
            break
        
        
    for key,lists in graph.items():
        if lists[1] >= 2 and lists[0] >= 2:
            answer[3] += 1
        elif lists[1] == 0:
            answer[2] += 1
    answer[1] = graph[main_deg][1] - (answer[2] + answer[3])

    
    return answer