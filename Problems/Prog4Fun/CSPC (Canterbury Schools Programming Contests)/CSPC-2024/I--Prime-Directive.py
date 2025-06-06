# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9684&cmid=4328&page=9

inputs = map(int, input().split())
output = []

def prime_counter(endpoint):
    counter = 0
    num = 2

    while num <= endpoint:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            counter += 1
            if num == endpoint:
                return counter
        num += 1

    return 0

for i in inputs:
    position = prime_counter(i)
    if position > 0:
        print(chr(position + 64), end="")