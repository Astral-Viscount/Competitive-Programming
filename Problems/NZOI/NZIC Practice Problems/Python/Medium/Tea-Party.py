# https://train.nzoi.org.nz/problems/870

import operator

n, k = map(int, input().split())

tea = ["G","C","E","P","L","S"]
favourite_tea = {}
stock = {}
person = {}

for _ in range(n):
    name, fav_tea = input().split()
    favourite_tea[name] = fav_tea

for _ in range(n):
    person_stock = input().split()
    stock[person_stock[0]] = list(map(int, person_stock[1::]))

for _ in range(k):
    person[input()] = 0

for i in range(len(tea)):
    count = operator.countOf(my_dict.values(), target_value)

print(tea)
print(favourite_tea)
print(stock)
print(person)