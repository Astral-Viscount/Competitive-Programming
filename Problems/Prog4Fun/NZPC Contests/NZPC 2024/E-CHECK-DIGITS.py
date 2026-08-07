# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11737&cmid=4329&page=5

while True:
    num = input()

    if num == "0":
        break

    total = 0
    count = 2

    for i in range(len(num) - 1, -1, -1):
        total += int(num[i]) * count
        count += 1

    total = 11 - (total % 11)

    if 1 <= total <= 9:
        print(f"{num} -> {num}{total}")
    elif total == 11:
        print(f"{num} -> {num}0")
    elif total == 10:
        print(f"{num} -> rejected")
