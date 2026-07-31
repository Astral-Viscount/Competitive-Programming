# https://cses.fi/problemset/task/1094

n = int(input())
numbers = list(map(int, input().split()))

counter = 0
prev_num = numbers[0]

for i in range(1, n):

    current_num = numbers[i]

    if prev_num > current_num:
        gap = prev_num - current_num
        prev_num = current_num + gap
        
        counter += gap

    else:
        prev_num = current_num

print(counter)