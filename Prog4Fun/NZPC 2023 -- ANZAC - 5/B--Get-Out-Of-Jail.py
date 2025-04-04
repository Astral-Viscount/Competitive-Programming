# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9493&cmid=3529&page=2

no_double = True

for _ in range(3):
    a , b = map(int, input().split())

    if a == b:
        print(f"Doubles. Move forwards {a + b} squares.")
        no_double = False
        break

if no_double:
    card = input()

    if card == 'y':
        print(f"Use card. Move forwards {a + b} squares.")
    else:
        print(f"$50 fine. Move forwards {a + b} squares.")
