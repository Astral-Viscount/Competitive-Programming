# https://train.nzoi.org.nz/problems/1510
# make 2d array
# check column by column

n , m = map(int, input().split())
t = input()

array = [t[i:i+n] for i in range(0, (n * m), n)]
arr_2d = []

for chunks in array:
    li = list(chunks)
    arr_2d.append(li)

best = []
change = 0

for column in range(n):
    count = {}

    for row in range(m):
        letter = arr_2d[row][column]

        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    
    freq = max(count, key=count.get)
    best.append(freq)
    change += (m - count[freq])


string = ''.join(best) * m
print(change)
print(string)
