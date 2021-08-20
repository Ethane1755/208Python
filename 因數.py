
    
import time

time_start = time.time() #開始計時

#要執行的程式碼，或函式
#要執行的程式碼，或函式

n = int(input("input number: ")) 
fac = [] 
for i in range(2, n): 
    if n % i == 0:
        fac.append(i) 
        continue
    else:
        pass
if len(fac) == 0: 
    print("是質數") 
else:
    print(fac)

time_end = time.time()    #結束計時

time_c= time_end - time_start   #執行所花時間
print('time cost', time_c, 's')