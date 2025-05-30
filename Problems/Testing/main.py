import time
start_time = time.time()

while True:
    a, b = map(int, input().split())
    
    if (a or b) != 0:
        print(a * b)
    else:
        break
                                                                
print("Process finished --- %s seconds ---" % (time.time() - start_time))