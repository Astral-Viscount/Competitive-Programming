# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11313&cmid=1851&page=10

stuff = input().split()

gnomes = {}

while stuff[0] != "END":
    name = stuff[0]
    g, b = map(int, stuff[1::])

    current_g, current_b = gnomes.get(name, (0, 0))
    gnomes[name] = (current_g + g, current_b + b)

    stuff = input().split()

bad = []

for key, value in gnomes.items():
    if (value[0] / value[1]) < 2:
        bad.append(key)

if bad:
    for i in bad:
        print(f"{i} needs to be dealt with.")
else:
    print("The world is safe for now.")