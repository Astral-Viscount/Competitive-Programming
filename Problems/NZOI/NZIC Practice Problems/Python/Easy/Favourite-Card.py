# https://train.nzoi.org.nz/problems/31

fav_card = list(map(int, input().split()))

cards = 0

for i in range(fav_card[0]):
    card = int(input())
    if card == fav_card[1]:
        break
    cards += 1

print(cards)
