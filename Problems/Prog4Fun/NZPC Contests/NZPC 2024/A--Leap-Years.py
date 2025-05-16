# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=8737&cmid=4329&page=1

n = int(input())

for _ in range(n):
    year = int(input())

    if year < 2024:
        sentence = "was a"
    elif year == 2024:
        sentence = "is a"
    else:
        sentence = "will be a"

    leap = "leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "common year"
    
    print(f"{year} {sentence} {leap}.")
