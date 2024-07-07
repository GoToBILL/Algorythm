def solution(commands):
    
    real_val = [["EMPTY" for i in range(51)] for j in range(51)]
    parent = [[[i,j] for j in range(51)] for i in range(51)]
    def find_parent(x_li):
        x,y = x_li[0],x_li[1]
        if x == parent[x][y][0] and y == parent[x][y][1]:
            return x_li
        parent[x][y] = find_parent(parent[x][y])
        real_val[x][y] = real_val[parent[x][y][0]][parent[x][y][1]]
        return parent[x][y]
    
    def merge(li1,li2):
        par1 = find_parent(li1)
        par2 = find_parent(li2)
        
        if li1 == li2 or par1 == par2:
            return
        if real_val[li1[0]][li1[1]] == "EMPTY" and real_val[li2[0]][li2[1]] != 'EMPTY':
            parent[par1[0]][par1[1]] = par2
        else:
            parent[par2[0]][par2[1]] = par1
         

    answer = []
    for string in commands:
        lists_str = string.split(" ")
        if lists_str[0] == "UPDATE":
            
            if len(lists_str) == 3:
                for i in range(1,51):
                    for j in range(1,51):
                        par = find_parent([i,j])
                        if real_val[par[0]][par[1]] == lists_str[1]:
                            real_val[par[0]][par[1]] = lists_str[2]
            
            else:
                x = int(lists_str[1])
                y = int(lists_str[2])
                par = find_parent([x,y])
                real_val[par[0]][par[1]] = lists_str[3]
                
        elif lists_str[0] == "MERGE":
            lists_int = list(map(int,lists_str[1:]))
            merge(lists_int[0:2],lists_int[2:])
            
        elif lists_str[0] == "UNMERGE":
            lists_int = list(map(int,lists_str[1:]))
            
            par = find_parent(lists_int)
            tmp = real_val[par[0]][par[1]]
            reset_list = []
            for i in range(1,51):
                for j in range(1,51):
                    par_i_j = find_parent([i,j])
                    if par_i_j == par:
                        reset_list.append([i,j])

            for i,j in reset_list:
                parent[i][j] = [i,j]
                real_val[i][j] = "EMPTY"
            real_val[lists_int[0]][lists_int[1]] = tmp
            
        elif lists_str[0] == "PRINT":
            lists_int = list(map(int,lists_str[1:]))
            par = find_parent(lists_int)
            answer.append(real_val[par[0]][par[1]])

    return answer