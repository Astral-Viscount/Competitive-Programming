# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/view.php?id=2796

num = int(input())
people = int(input())

guesses = {}
best = num
winner = ''

for i in range(people):
    name = input()
    bean = int(input())
    guesses[name] = bean

for name, guess in guesses.items():
    value = abs(num - guess)
    if value < best:
        best = value
        winner = name

print(winner)
