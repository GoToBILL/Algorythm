n = int(input())
for i in range(n):
     mid = input()
     flag = 1
     sum = 0
     for j in range(len(mid)):
          if mid[j] == "O":
               sum += flag
               if (j+1 != len(mid)) and mid[j+1] == "O":
                    flag += 1
               else:
                    flag = 1
     print(sum)