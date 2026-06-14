# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11316&cmid=5965&page=1

n = int(input())
total = 0
rounded = 0
change = 0

for _ in range(n):
    total += float(input())

pay = float(input())

total = round(total, 2)
cents = int(round(total * 100))
last_digit = cents % 10

if 1 <= last_digit <= 4:
    rounded_cents = cents - last_digit
else:
    rounded_cents = cents + (10 - last_digit) if last_digit != 0 else cents

rounded = rounded_cents / 100.0
change = pay - rounded

print(f"Total price: ${total:.2f}\nRounded price: ${rounded:.2f}\nChange: ${change:.2f}")