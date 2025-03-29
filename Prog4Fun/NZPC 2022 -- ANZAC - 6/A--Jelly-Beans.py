# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/view.php?id=2796

num = int(input())
people = int(input())

best = None
difference = float('inf')
winner = ''

for i in range(people):
    name = input()
    bean = int(input())

    value = abs(num - bean)

    if value < difference:
        difference = value
        best = value
        winner = name

print(winner)
