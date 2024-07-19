from collections import defaultdict as df
import math

def solution(fees, records):
    answer = []
    
    def return_default():
        # 0 -> total sum , 1 -> in 기록 , 2 -> 마지막이 in or out
        return [0,0,0]
    def time_cnt(a,b):
        a_hour = int(a[0:2])
        a_minute = int(a[3:5])
        b_hour = int(b[0:2])
        b_minute = int(b[3:5])
        return ((b_hour-a_hour) * 60 + (b_minute-a_minute))
    def answer_cnt():
        sorted_list = sorted(dict_car)
        for x in sorted_list:
            diff = dict_car[x][0] - fees[0]
            SUM = (fees[1] if diff <= 0 else fees[1] + math.ceil(diff/fees[2])*fees[3])
            answer.append(SUM)
    
    dict_car = df(return_default)
    for procedure in records:
        t, car_num, acting = procedure.split(" ")
        
        if acting == "IN":
            dict_car[car_num][1] = t
            dict_car[car_num][2] = 0
        elif acting == "OUT":
            dict_car[car_num][0] += time_cnt(dict_car[car_num][1],t)
            dict_car[car_num][2] = 1
    for x in dict_car:
        if dict_car[x][2] == 0:
            dict_car[x][0] += time_cnt(dict_car[x][1],"23:59")
    answer_cnt()
    return answer