

def solution(cap, n, deliveries, pickups):
    answer = 0
    s_deli = [[i+1,deliveries[i]] for i in range(n) if deliveries[i] != 0]
    s_bring = [[i+1,pickups[i]] for i in range(n) if pickups[i] != 0]
    
    def stack_sol(st):
        result = 0
        max_deli = 0
        while st:
            out_deli = st.pop()
            if out_deli[0] > max_deli:
                max_deli = out_deli[0]

            if result + out_deli[1] > cap:
                out_deli[1] = result + out_deli[1] - cap
                st.append(out_deli)
                return max_deli
            result += out_deli[1]
        return max_deli
    while s_deli or s_bring:
        answer += max(stack_sol(s_deli),stack_sol(s_bring)) * 2
                  
    return answer

