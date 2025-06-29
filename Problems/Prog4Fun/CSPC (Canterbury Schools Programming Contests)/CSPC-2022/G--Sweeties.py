# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9723&cmid=2793&page=6

n = int(input())

stock = {}

for _ in range(n):
    s, j, c = input().split()
    j = int(j)
    c = int(c)

    stock[s] = (j, c)

while True:
    sweet, amount = input().split()

    if sweet == "#" and amount == "#":
        break

    amount = int(amount)

    j = stock[sweet][0]
    c = stock[sweet][1]
    
    
   
