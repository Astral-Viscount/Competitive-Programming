# https://train.nzoi.org.nz/problems/19

numbers = []
steps_num = []

num = int(input())

while num != 0:
    numbers.append(num)
    num = int(input())

for number in numbers:
    steps = 0
    while number != 1:
        if number %2 == 0:
            number /= 2
            steps += 1           
        else:
            number = (3 * number) + 1
            steps += 1
    steps_num.append(steps)

for nums in steps_num:
    print(nums)

