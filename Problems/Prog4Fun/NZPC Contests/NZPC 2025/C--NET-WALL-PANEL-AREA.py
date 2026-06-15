# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11316&cmid=5965&page=2

w, h = map(int, input().split())
n = int(input())

w = w / 1000
h = h / 1000

total_wall = w * h

total_pane = 0

for _ in range(n):
    a, b = map(int, input().split())
    a = a / 1000
    b = b/ 1000
    total_pane += round(a * b, 2)

nwpa = total_wall - total_pane

if nwpa <= 0:
    print("Please check the dimensions.")
else:
    print(f"The Net Wall Panel Area is {nwpa:.2f} square metres.")