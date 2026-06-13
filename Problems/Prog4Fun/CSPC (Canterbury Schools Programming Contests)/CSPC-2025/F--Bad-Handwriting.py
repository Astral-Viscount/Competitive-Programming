# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11308&cmid=5961&page=1&mdlscrollto=2548

n = int(input())

for _ in range(n):
    a, b, c = input().split()

    if a == "?" and b == "?":
        print("remeasure")
    elif a == "?":
        print(f"{int(int(c)/int(b))} {b} {c}")
    elif b == "?":
        print(f"{a} {int(int(c)/int(a))} {c}")
    elif c == "?":
        print(f"{a} {b} {int(a)*int(b)}")
    else:
        print(f"{a} {b} {c}")