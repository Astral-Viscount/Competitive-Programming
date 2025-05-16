import time
start_time = time.time()

a = 'MaHi'
b = a.replace(a[0], a[0].title())
print(b)

print("Process finished --- %s seconds ---" % (time.time() - start_time))