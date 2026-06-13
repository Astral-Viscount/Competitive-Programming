# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11308&cmid=5961&page=1&mdlscrollto=600

a, b = map(int, input().split())

if a == b:
    print("Keep trying!")
elif a > b:
    print("OMG!")
else:
    print("Improved!")