# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11316&cmid=5965&page=3

n = int(input())

for _ in range(n):
    sentence = input().split()
    for idx, word in enumerate(sentence):
        if len(word) <= 3:
            sentence[idx] = word
        else:
            sentence[idx] = word[0] + word[1:-1][::-1] + word[-1]
    print(*sentence)