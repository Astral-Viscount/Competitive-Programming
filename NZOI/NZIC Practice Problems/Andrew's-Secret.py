# https://train.nzoi.org.nz/problems/24

numbers = list(map(int, input().split()))

print(min(numbers), max(numbers), sum(numbers)//len(numbers))
