# https://train.nzoi.org.nz/problems/1176

nails = [input() for _ in range(5)]
best = True
ok = False

if len(set(nails[0])) != len(nails[0]):
    for i in range(1, 5):
        if len(nails[i]) % 2 == 0:
            best = False

else:
    best = False
    letter = len(nails[1])
    for j in range(2, 5):
        if len(nails[j]) < letter :
            letter = len(nails[j])
            ok = True
        else:
            ok = False
            break

if best:
    print("best")
elif ok:
    print("ok")
else:
    print("bad")
