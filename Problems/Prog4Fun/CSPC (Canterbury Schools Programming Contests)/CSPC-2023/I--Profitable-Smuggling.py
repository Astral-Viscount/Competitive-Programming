# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9722&cmid=3199&page=9

n = int(input())

average = {
    "SP": 34,
    "LT": 18,
    "E152": 129,
    "HF": 8,
    "KC": 475
}

sales = 0
purchases = 0

for _ in range(n):
    while True:
        code, amount, price = input().split()

        if code == "#":
            break

        amount = int(amount)
        price = int(price)

        purchases += amount * price

        price = average[code]
        sales += amount * price

print(sales - purchases)
