import time

time_start = time.time() #開始計時

#要執行的程式碼，或函式
#要執行的程式碼，或函式
n = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997
b = 1
while b < 100000000:
    b = b+1
if n%b == 0:
    print("不是質數")
else:
    print("是質數")



time_end = time.time()    #結束計時

time_c= time_end - time_start   #執行所花時間
print('time cost', time_c, 's')
